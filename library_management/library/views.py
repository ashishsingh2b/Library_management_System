from django.shortcuts import render,redirect
from .models import Book,Stundet
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def add_book(request):
    if request.method == "POST":
        name =request.POST['name']
        author=request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']

        books = Book.objects.create(name=name,author=author,isbn=isbn,category=category)
        books.save()
        alert = True
        return render(request,'add_book.html',{'alert':alert})
    return render(request,'add_book.html')

def view_books(request):
    books  = Book.objects.all()
    return render(request,'view_books.html',{'books':books})

def delete_book(request,myid):
    books = Book.objects.filter(id=myid)
    books.delete()
    return redirect("/viewbook/")

def student_rejistration(request):
    if request.method == "POST":
        usernname= request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone=request.POST['phone']
        branch=request.POST['branch']
        classroom=request.POST['classroom']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password != confirm_password:
            passnomatch=True
            return render(request,'Stu_reg.html',{'passnomathc':passnomatch})
        
        user = User.objects.create_user(username=usernname,email=email,password=password,first_name=first_name,last_name=last_name)
        student =Stundet.objects.create(user=user,phone=phone,branch=branch,classroom=classroom,roll_no=roll_no, phone = phone)

