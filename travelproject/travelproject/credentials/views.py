from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method=='POST':
        username =request.POST['Username']
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        email = request.POST['Email']
        password = request.POST['Password']
        cpassword = request.POST['Conform password']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter( email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)

            user.save();
            print('user created')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")