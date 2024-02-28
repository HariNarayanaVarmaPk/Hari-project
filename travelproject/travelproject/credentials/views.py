from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from django.contrib import auth, messages
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html', {'invalid_credentials': True})
    return render(request, 'login.html')

    

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
            return redirect('login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")