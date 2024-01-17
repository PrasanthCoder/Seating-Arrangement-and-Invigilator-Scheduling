# Introduction
## Automated Seating Arrangement and Invigilator Scheduling System
Our application is designed to streamline the exam logistics process by automating the seating arrangement of students in exam halls based on provided seating and student information. 
Additionally, it facilitates the efficient scheduling of invigilators to classrooms, taking into account their working hours. The system also offers automated email notifications, 
allowing for the timely dispatch of reminders to invigilators, such as one hour before exams. Faculty can also raise complaint tikets on the students who are cheating in the exam. The ticket directly goes to the dashboard of the admin. This comprehensive solution aims to save time, optimize resource allocation, and enhance communication efficiency, 
ultimately contributing to a smoother and more organized examination experience for both students and staff.

## Tech Stack
1. Django
2. python
3. HTML, CSS, Bootstrap
4. dotenv
5. Celery worker with CloudAMQP server.
6. SMTP
7. PostgreSQP

## Setup
1. First, Install all the requirements
2. Downnload and install Django, PostgreSQL.
3. Create any AMQP cloud server and create an instance. Link the instance to the application in the settings.py or using the .env file.
4. Setup Database settings as per your database instance created. Merge the models.
5. To run the application, first run the server and then run the celery worker on celery.py in the project directory. use --pool=solo attribute to the celery to get a single threaded process to get rid of errors.

Here are the commands that you can use
```
$ python manage.py runserver
```
To run the celery worker you can use this command
```
$ python -A epics.celery worker --loglevel=info --pool=solo
```
# Application Functions
## Seating Arrangement
The Student information and Subjects information should be given as an input in the form of excel sheets.
  
![student and subject information](application_images/student%20input.png)  
  
Then to get the seating arrangement, we have to give seating information and student registration information as input in the form of excel sheets.  
Here is an example of seating information.  
  
![seating information](application_images/seating%20positions.jpg)  
  
Each sheet in the excel file represent each room. Yellow means the seat is good to fill. Red means that seat is missing or damaged (Should not be filled).
  
![seating input](application_images/seating%20form.png)  

After filling the form, we will get an output excel file downloaded with students filled in the seatings given as per the constraints (No two students with same subject can be next to each other or beside each other)  
  
## Invigilator Scheduling
First we have to give faculty information in the input form using an excel sheet.
Then, we have to fill the scheduling information form to get the scheduling.  
  
![scheduling form](application_images/scheduling%20form.png)  

Then we can have output either as a print on the web or a download which include an excel sheet with scheduling information filled with faculty names in it as per the constraints.  Also, emails will be sent automatically as per the code.(The default code corresponds to current time as eta, we can change it to whichever time we want)  

![scheduling output](application_images/fac%20print.png)

## Faculty and Admin Panel
Faculty can login using their FacultyID and Password. THe password in the FacultyID + last four digits of their name.  

![faculty login](application_images/faculty%20login.png)

Here is the dashboard to raise tickets in the faculty login page.  

![faculty panel](application_images/fac%20dash.png)  

For admin also there is a login panel and dashboard. In the dashboard, all the raised tickets can be seen and can be removed if rectified.  

![admin panel](application_images/admin%20dash.png)  

Copyrights@PrasanthCoder
