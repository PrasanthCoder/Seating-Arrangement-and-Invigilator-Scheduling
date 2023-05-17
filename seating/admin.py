from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BTStudentInfo)
admin.site.register(BTSubjectInfo)
admin.site.register(BTRollLists)
admin.site.register(BTStudnetRegistrations)