from django.urls import path

from LibrarymanagementApp import views

urlpatterns = [
    path('',views.log_fun,name='log'),
    path('logdata',views.logdata_fun),

    path('adminreg',views.admin_reg,name='adminreg'),#it will open admin register page
    path('adminregdata',views.adminregdata_fun),

    path('studentreg',views.studentreg_fun,name='studentreg'),
    path('studentdata',views.studentdata_fun),

    path('home',views.home_fun,name='home'),

    path('addbook',views.addbook_fun,name='addbook'),#it will open add_book.html
    path('readaddedbook',views.readaddedbook_fun),#add book to Books model

    path('displaybook',views.displaybook_fun,name='displaybook'),#it will display Book table(opens display_book.html)
    path('update/<int:id>',views.updatebook_fun,name='update'),#it opens update_book.html and updates the book details
    path('Delete/<int:id>',views.deletebook_fun,name='Delete'),

    path('assignbook',views.assignbook_fun,name='assignbook'),#it opens assign_book.html
    path('getstudent',views.getstudent_fun,name='getstudent'),#it will get student and books related course using phno.entered
    path('asgnbook',views.asgnbook_fun,name='asgnbook'),#add assigned book data to issued book table

    path('assignedbook',views.assignedbook_fun,name='assignedbook'),#it will open assigned_book.html
    path('up/<int:id>',views.upassigned_fun,name='up'),#updates assigned book data and redirect to assignedbook.html
    path('del/<int:id>',views.delassigned_fun,name='del'), #delete the assigned book

    path('Studenthome',views.studenthome_fun,name='Studenthome'),#redirect to Stud_home.html
    path('studissuedbook',views.studissuedbook_fun,name='studissuedbook')








]