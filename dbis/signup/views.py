from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages
fn=''
ln=''
mobile=''
email=''
Password=''

# Create your views here.
def signup_action(request):
    global fn,ln,mobile,email,Password

    if(request.method=="POST"):
        obj =sql.connect(host="localhost",user='root',password='Rohandhiman2005@',database='website')
        cursor=obj.cursor()
        
        data=request.POST
        for key,value in data.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="phone":
                mobile=value
            if key=="email":
                email=value
            if key=="password":
                Password=value
        
        c="insert into user_details Values('{}','{}','{}','{}','{}')".format(fn,ln,email,Password,mobile)
        cursor.execute(c)
        obj.commit()
        # obj.close()
        messages.success(request, 'Registration completed successfully!')
        return redirect('login_action') 
    return render(request,'signup_page.html')


 

    