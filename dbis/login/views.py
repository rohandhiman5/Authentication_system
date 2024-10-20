from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages
Email=''
Password=''
# Create your views here.
def login_action(request):
    global Email,Password
    if request.method=="POST":
        m =sql.connect(host="localhost",user='root',password='Rohandhiman2005@',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                Email=value
            if key=="password":
                Password=value
        
        c="select * from user_details where email='{}' and password='{}'".format(Email,Password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if not t:  # If the tuple is empty, the login failed
            messages.error(request, "Invalid email or password. Please try again.")  # Add error message
            return redirect('login_action')  # Pass the error message back to the login page   
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')