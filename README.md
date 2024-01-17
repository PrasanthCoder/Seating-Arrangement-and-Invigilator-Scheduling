# Introduction
## Automated Seating Arrangement and Invigilator Scheduling System
Our application is designed to streamline the exam logistics process by automating the seating arrangement of students in exam halls based on provided seating and student information. 
Additionally, it facilitates the efficient scheduling of invigilators to classrooms, taking into account their working hours. The system also offers automated email notifications, 
allowing for the timely dispatch of reminders to invigilators, such as one hour before exams. This comprehensive solution aims to save time, optimize resource allocation, and enhance communication efficiency, 
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
The Student information and Subjects information should be given as an input

   
