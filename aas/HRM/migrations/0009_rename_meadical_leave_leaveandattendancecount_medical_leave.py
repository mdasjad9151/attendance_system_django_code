# Generated by Django 4.1.7 on 2023-04-10 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HRM', '0008_rename_personal_leave_leaveandattendancecount_personal_leave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaveandattendancecount',
            old_name='meadical_leave',
            new_name='medical_leave',
        ),
    ]
