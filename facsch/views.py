from django.shortcuts import render
# Create your views here.
from django.shortcuts import redirect
import pandas as pd
import xlsxwriter as xlsxwriter
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .tasks import send_mail_func
from datetime import timedelta
from django.utils import timezone

# Create your views here.

def input(request):
    if request.method == 'POST':
        xcel_file = request.FILES['faculty']
        fac_file = pd.read_excel(xcel_file)
        for row in fac_file.iterrows():
            faculty_instance = BTFacultyInfo(
                FacultyId = row['FacultyId'],
                Name = row['Name'],
                Dept = row['dept'],
                Phone = row['Phone'],
                Email = row['Email'],
                Working = row['Working'],
                WorkingHours = row['WorkingHours']
            )
            faculty_instance.save()

    else:
        return render(request, 'faculty.html')

def facsch(request):
    if request.method == 'POST':
        print('off')
        days = request.POST.get('days')
        rooms = request.POST.get('rooms')
        sessions = request.POST.get('sessions')
        hours = request.POST.get('hours')
        choice = request.POST.get('choose')

        ###
        ###

        writer = pd.ExcelWriter('output_scheduling.xlsx', engine='xlsxwriter') # creating an excel file

        #creating list in all faculty id's
        fac_list = list(BTFacultyInfo.objects.values('FacultyId').order_by('WorkingHours', 'FacultyId').values_list('FacultyId', flat=True).distinct())
        # Define the pattern string for the row and column names
        pattern1 = 'd{} s{}'
        pattern2 = 'room {}'
        # Create a list of row names using the pattern string
        col_names = [pattern1.format(i,j) for i in range(1, int(days)+1) for j in range(1,int(sessions)+1)]
        row_names = [pattern2.format(i) for i in range(1, int(rooms)+1)]

        df = pd.DataFrame(index=row_names, columns=col_names) # creating dataframe

        print(df)

        for col in df.columns:
            for index, row_value in df[col].items():
                fac1 = BTFacultyInfo.objects.get(FacultyId=fac_list[0])
                fac2 = BTFacultyInfo.objects.get(FacultyId=fac_list[1])
                df.at[index,col] = fac1.Name + ', ' + fac2.Name
                fac1.WorkingHours += int(hours)
                fac2.WorkingHours += int(hours)
                fac1.save()
                print(fac1.WorkingHours)
                fac2.save()
                ###
                to_email1 = BTFacultyInfo.objects.get(FacultyId = fac_list[0])
                to_email2 = BTFacultyInfo.objects.get(FacultyId = fac_list[1])
                recipient1 = to_email1.Email
                recipient2 = to_email2.Email
                subject = 'Invigilation duty'
                message = 'Sir, your invigilation is on ' + col + '. please go to assigned room no ' + index
                send_time = timezone.now()  # schedule the email to be sent one hour from now
                send_mail_func.apply_async(args=[recipient1, subject, message], eta=send_time)
                send_mail_func.apply_async(args=[recipient2, subject, message], eta=send_time)
                ###
                fac_list = list(BTFacultyInfo.objects.values('FacultyId').order_by('WorkingHours', 'FacultyId').values_list('FacultyId', flat=True).distinct())
        response_content = []
        for col in df.columns:
            response_content.append(f"\n{col}")
            for index, row_value in df[col].items():
                response_content.append(f"{index}  {row_value}")

        response_text = "\n".join(response_content)
        response = HttpResponse(response_text, content_type="text/plain")

        df.to_excel(writer, sheet_name='Scheduling')
        writer.save()

        with open('output_scheduling.xlsx', 'rb') as f:
            buffer = f.read()
        
        response1 = HttpResponse(buffer, content_type='application/vnd.ms-excel')
        response1['Content-Disposition'] = 'attachment; filename="output_scheduling.xlsx"'

        print(choice)
        if(choice == "Download"):
            return response1
        else:
            return response
    else:
        return render(request, 'facsch.html')


@never_cache
def faclogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if BTFacultyInfo.objects.filter(FacultyId = username).exists():
            obj = BTFacultyInfo.objects.get(FacultyId = username)
            if password == username + obj.Name[-4:]:
                return render(request, 'facdash.html')
            else:
                return HttpResponse("userid or password are incorrect")
        else:
            return HttpResponse("userid or password are incorrect in first loop")
        
    else:
        return render(request, 'faclogin.html')


def facdash(request):
    if request.method == 'POST':
        rollno = request.POST.get('rollno')
        malmethod = request.POST.get('malmethod')
        desc = request.POST.get('description')
        if MalComplaints.objects.filter(RollNo = rollno).exists():
            return HttpResponse("Ticket with this roll number already registered")
        mal_instance = MalComplaints(
                RollNo = rollno,
                MalMethod = malmethod,
                Description = desc
        )
        mal_instance.save()
        return render(request, 'ticketsucc.html')

    else:
        if request.META.get('HTTP_REFERER', '').endswith('/sch/facdash/'):
            return render(request, 'facdash.html')
        return render(request, 'faclogin.html')

def adminlogin(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = user, password = password)

        if(user is not None):
            auth.login(request,user)
            tiks = list(MalComplaints.objects.all())
            records_list = []
            for record in tiks:
                record_dict = {
                    'RollNo': record.RollNo,
                    'MalMethod': record.MalMethod,
                    'Description': record.Description,
                }
                records_list.append(record_dict)
            return render(request, 'admindash.html', {'tickets' : records_list})
        else:
            messages.info(request,'invalid credentials')
            return HttpResponse("userid or password is incorrect")
    else:
        return render(request, "adminlogin.html")
    
def admindash(request):
    if request.method == 'POST':
        tktid = request.POST.get('ticketid')
        tkt = MalComplaints.objects.get(RollNo = tktid)
        tkt.delete()
    tiks = list(MalComplaints.objects.all())
    records_list = []
    for record in tiks:
        record_dict = {
            'RollNo': record.RollNo,
            'MalMethod': record.MalMethod,
            'Description': record.Description,
        }
        records_list.append(record_dict)
    return render(request, 'admindash.html', {'tickets' : records_list})