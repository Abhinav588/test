# Generated by Django 4.1 on 2022-09-06 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0004_rename_photo_student_user_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='User_Photo',
            new_name='User_Photos',
        ),
    ]