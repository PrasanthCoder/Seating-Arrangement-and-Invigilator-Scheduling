from django.db import models
# Create your models here.

# model for student information
class BTStudentInfo(models.Model):
    CYCLE_CHOICES = (
        (10,'PHYSICS'),
        (9,'CHEMISTRY')
    )
    RegNo = models.IntegerField()
    RollNo = models.IntegerField()
    Name = models.CharField(max_length=255)
    Regulation = models.FloatField()
    Dept = models.IntegerField()
    AdmissionYear = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Category = models.CharField(max_length=30)
    GuardinaName = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField()
    Address1 = models.TextField()
    Address2 = models.TextField(null=True)
    Cycle = models.IntegerField(default=0, choices=CYCLE_CHOICES)

    def __str__(self):
        return str(self.RollNo) + ' ' + self.Name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['RegNo'], name='unique_BTStudnetInfo_RegNo'),
            models.UniqueConstraint(fields=['RollNo'], name='unique_BTStudentInfo_RollNo')
        ]


# model for subject information
class BTSubjectInfo(models.Model):
    Year = models.IntegerField()
    Sem = models.IntegerField()
    Regulation = models.FloatField()
    Mode = models.CharField(max_length=1)
    Dept = models.IntegerField()
    SubId = models.IntegerField()
    SubCode = models.CharField(max_length=10)
    SubName = models.CharField(max_length=100)
    Credits = models.IntegerField()
    Type = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)

    def __str__(self):
        return str(self.SubCode) + ' ' + self.SubName
    

# model for rollno
class BTRollLists(models.Model):
    CYCLE_CHOICES = (
        (10,'PHYSICS'),
        (9,'CHEMISTRY')
    )
    Student = models.ForeignKey(BTStudentInfo, on_delete=models.CASCADE, default='1')
    Cycle = models.IntegerField(default=0, choices=CYCLE_CHOICES)
    Section = models.CharField(max_length=2, default='1')


# model for course registered students
class BTStudnetRegistrations(models.Model):
    Student = models.ForeignKey(BTRollLists, on_delete=models.CASCADE, default='1')
    Mode = models.IntegerField()
    Sub_Id = models.ForeignKey(BTSubjectInfo, on_delete=models.CASCADE, db_column="sub_id")



