# Generated by Django 4.1.7 on 2023-05-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facsch', '0003_btfacultyinfo_workinghours'),
    ]

    operations = [
        migrations.CreateModel(
            name='MalComplaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNo', models.CharField(max_length=20)),
                ('MalMethod', models.CharField(max_length=225)),
                ('Description', models.TextField()),
            ],
        ),
    ]
