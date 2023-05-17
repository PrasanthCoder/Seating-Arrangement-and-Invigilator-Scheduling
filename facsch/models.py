from django.db import models

# Create your models here.

# model for faculty information

class BTFacultyInfo(models.Model):
    FacultyId = models.IntegerField(default=100)
    Name = models.CharField(max_length=255)
    Phone = models.TextField()
    Email = models.CharField(max_length=255)
    Dept = models.IntegerField()
    Working = models.BooleanField()
    WorkingHours = models.IntegerField(default=0)

    class Meta:
        db_table = 'BTFacultyInfo'
        constraints = [models.UniqueConstraint(fields=['FacultyId'], name='unique_BTfacultyinfo_facultyid')]
        managed = True

class MalComplaints(models.Model):
    RollNo = models.CharField(max_length=20)
    MalMethod = models.CharField(max_length=225)
    Description = models.TextField()