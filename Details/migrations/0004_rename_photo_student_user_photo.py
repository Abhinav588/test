# Generated by Django 4.1 on 2022-09-06 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0003_student_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Photo',
            new_name='User_Photo',
        ),
    ]