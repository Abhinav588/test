from django.contrib import admin

from Details.models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','First_Name','Last_Name','Gender','Date_of_Birth','Mobile_Number','E_Mail','Adm_Num_and_Date','deptmt','Father_name','Mother_name','Father_mob','Mother_mob','Address')
