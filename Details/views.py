from http.client import OK
import os
from tkinter import *
from tkinter import messagebox
import tkinter
from django.shortcuts import redirect, render
from Details.models import Student

def showpage(request):
    return render(request,'Details.html')

def add_student(request):
    if request.method=='POST':
        F_name = request.POST['Sfname']
        L_name =  request.POST['Slname']
        gend =  request.POST['gender']
        date_ob = request.POST['DOB']
        mobile = request.POST['stnum']
        eMail = request.POST['Email']
        Adm =  request.POST['AdmNum']
        dep = request.POST['Department']
        Father =  request.POST['Fathname']
        Mother =  request.POST['mothname']
        F_mob =  request.POST['FathMnum']
        M_mob =  request.POST['MothMnum']
        address =  request.POST['addrs']
        try:
            pic = request.FILES['st_img']
        except:
            pic = None
        stud = Student(First_Name=F_name,
                Last_Name=L_name, Gender=gend, Date_of_Birth=date_ob,
                Mobile_Number=mobile, E_Mail=eMail, Adm_Num_and_Date=Adm,
                deptmt=dep, Father_name=Father, Father_mob=F_mob,Mother_name=Mother,
                 Mother_mob=M_mob, Address=address,User_Photo=pic)
        stud.save()
        return redirect('showsaved')
def showsaved(request):
    studt=Student.objects.all()
    return render(request,'show.html',{'show':studt})

def editpage(request,od):
    stude=Student.objects.get(id=od)
    return render(request,'Edit.html',{'edit':stude})
    
def editing(request,od):
    if request.method=='POST':
        stude=Student.objects.get(id=od)
        stude.First_Name = request.POST.get('fname')
        stude.Last_Name = request.POST.get('Slname')
        stude.Gender = request.POST.get('gender')
        stude.Date_of_Birth = request.POST.get('DOBN')
        stude.Mobile_Number = request.POST.get('tnum')
        stude.E_Mail = request.POST.get('E-mail')
        stude.Adm_Num_and_Date = request.POST.get('Admnum')
        stude.deptmt = request.POST.get('department')
        stude.Father_name = request.POST.get('fathname')
        stude.Mother_name = request.POST.get('mothname')
        stude.Father_mob = request.POST.get('fathMnum')
        stude.Mother_mob = request.POST.get('mothMnum')
        stude.Address = request.POST.get('addr')
        try:
            if len(request.FILES)!=0:
                if len(stude.User_Photo) >0:
                    os.remove(stude.User_Photo.path)
                stude.User_Photo = request.FILES['Nst_img']
        except:
            if len(stude.User_Photo) >0:
                os.remove(stude.User_Photo.path)
            stude.User_Photo = request.FILES['st_img']
        stude.save()
        return redirect('showsaved')
    return render(request,'Edit.html')
def delete(request,od):
    stude=Student.objects.filter(id=od)
    sh = tkinter.Tk()
    sh.withdraw()
    sh.attributes('-topmost',True)
    sh.focus_force()
    a=messagebox.askokcancel('Warning','Are you sure. Do you wan to Delete?')
    print(a)
    if a==True:
        stude.delete()
        return redirect('showsaved')
    elif a==False:
        return redirect('showsaved')
    sh.mainloop()
    return redirect('showsaved')
