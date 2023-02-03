from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect


# Create your views here.
from LibrarymanagementApp.models import Student, Course, Books, Issue_book


def log_fun(request):
    return render(request,'login.html',{'data':''})


def admin_reg(request):
    return render(request,'admin_reg.html',{'data':''})


def adminregdata_fun(request):
    user_name = request.POST['txtUserName']
    user_email = request.POST['txtEmail']
    user_password = request.POST['txtPassword']

    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, 'admin_reg.html', {'data': 'Username or email already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name, email=user_email, password=user_password)
        u1.save()
        return redirect('log')

user_name=''
def logdata_fun(request):
    user_name = request.POST['txtUserName']
    user_password = request.POST['txtPassword']
    user1 = authenticate(username=user_name,password=user_password)
    if user1 is not None:
        if user1.is_superuser:
            return render(request,'home.html')
        else:
            return render(request,'login.html',{'data':'User is not a superuser'})
    elif Student.objects.filter(Q(Stud_Name=user_name) & Q(Stud_Password=user_password)).exists():
        return render(request,'Stud_home.html')
    else:
        return render(request, 'login.html',{'data':'Enter proper username and password'})


def studentreg_fun(request):
    course = Course.objects.all()
    return render(request,'student_reg.html',{'Course_Data':course})


def studentdata_fun(request):
    StudName = request.POST['txtName']
    StudPhno = request.POST['txtPhno']
    StudSem = request.POST['txtSem']
    StudPassword=request.POST['txtPassword']
    StudCourse = Course.objects.get(Course_Name=request.POST['ddlCourse'])
    if Student.objects.filter(Q(Stud_Name=StudName)).exists():
        return render(request,'student_reg.html',{'data':'username already exists'})
    else:
        s1 = Student(Stud_Name=StudName,Stud_Phno=StudPhno,Stud_Sem=StudSem,Stud_Password=StudPassword,Stud_Course=StudCourse)
        s1.save()
    return redirect('log')


def home_fun(request):
    return render(request,'home.html')


def addbook_fun(request):
    course= Course.objects.all()
    return render(request,'add_book.html',{'Course_Data':course})


def readaddedbook_fun(request):
    b1=Books()
    b1.Book_Name=request.POST['txtBookName']
    b1.Author_Name=request.POST['txtAuthorName']
    b1.Course_Id=Course.objects.get(Course_Name=request.POST['ddlCourse'])
    b1.save()
    return redirect('addbook')


def displaybook_fun(request):
    b1=Books.objects.all()
    return render(request,'display_book.html',{'data':b1})


def updatebook_fun(request,id):
    b1=Books.objects.get(id=id)
    course=Course.objects.all()

    if request.method == 'POST':
        b1.Book_Name = request.POST['txtBookName']
        b1.Author_Name = request.POST['txtAuthorName']
        b1.Course_Id = Course.objects.get(Course_Name=request.POST['ddlCourse'])
        b1.save()
        return redirect('displaybook')
        
    return render(request,'update_book.html',{'data':b1,'Course_Data':course})


def deletebook_fun(id):
    b1=Books.objects.get(id=id)
    b1.delete()
    return redirect('displaybook')


def assignbook_fun(request):
    return render(request,'assign_book.html',{'Book_Data':'','data':''})


def getstudent_fun(request):

    s1=Student.objects.get(Stud_Phno=request.POST['txtPhno'])
    b1 = Books.objects.filter(Course_Id=s1.Stud_Course_id)
    return render(request,'assign_book.html',{'Book_Data':b1,'data':s1})


def asgnbook_fun(request):
    i1=Issue_book()
    i1.Student_Name=Student.objects.get(Stud_Name=request.POST['txtName'])
    i1.Book_Name = Books.objects.get(Book_Name=request.POST['ddlBook'])
    i1.Start_Date = request.POST['txtstartdate']
    i1.End_Date = request.POST['txtenddate']
    i1.save()
    return redirect('assignbook')


def assignedbook_fun(request):
    i1=Issue_book.objects.all()
    return render(request,'assigned_books.html',{'data':i1})


def upassigned_fun(request,id):
    i1 = Issue_book.objects.get(id=id)
    books = Books.objects.all()
    s1=Student.objects.all()

    if request.method == 'POST':
        i1.Student_Name = Student.objects.get(Stud_Name=request.POST['ddlStudentname'])
        i1.Book_Name = Books.objects.get(Book_Name=request.POST['ddlBook'])
        i1.Start_Date = request.POST['txtStartDate']
        i1.End_Date = request.POST['txtEndDate']
        i1.save()
        return redirect('assignedbook')

    return render(request, 'upassigned.html', {'data': i1, 'Book_Data': books, 'student_data':s1})


def delassigned_fun(request,id):
    i1=Issue_book.objects.get(id=id)
    i1.delete()
    return redirect('assigned_books.html')


def studenthome_fun(request):
    return redirect('Stud_home.html')


def studissuedbook_fun(request):
    i1=Issue_book.objects.all()

    return render(request,'Studissuedbook.html',{'data':i1})
