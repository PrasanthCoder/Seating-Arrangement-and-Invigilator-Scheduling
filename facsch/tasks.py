from __future__ import absolute_import, unicode_literals
from django.conf import settings
from celery import shared_task
from django.core.mail import send_mail
from .models import *

@shared_task(bind=True)
def send_mail_func(self, to_email, subject, message):
    #operations
    send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email], fail_silently=False)
    return "Done"