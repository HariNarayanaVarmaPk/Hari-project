import os
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login as auth_login
from django .contrib.auth import logout as auth_logout
from django.http import  HttpResponseNotAllowed
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CinemaForm
from django.contrib.auth.models import User
from .  models import Cinema
from django.core.paginator import Paginator



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        
        storage = messages.get_messages(request)
        for message in storage:
            pass
        
        # Validate form data
        if not (username and email and first_name and last_name and password):
            messages.error(request, 'All fields are required.')
            return render(request, 'register.html', {'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name})
        
        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html', {'email': email, 'first_name': first_name, 'last_name': last_name})
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'register.html', {'username': username, 'first_name': first_name, 'last_name': last_name})
        else:
            # If neither username nor email exists, proceed with registration
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            messages.success(request, f'Registration successful. Welcome, {username}! You can now log in to your account.')
            return redirect('login')  # Redirect to login page
    else:
        return render(request, 'register.html')
    
    
    

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('view')
    else:
        form = AuthenticationForm()
        
    
    storage = messages.get_messages(request)
    for message in storage:
        pass
    
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    
    return redirect('register')


def view_profile(request):
    user = request.user
    return render(request, 'profile_view.html', {'user': user})




def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        # Handle profile editing form submission
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('view_profile')
    return render(request, 'profile_edit.html', {'user': user})



def add(request):
    if request.method == 'POST':
        form = CinemaForm(request.POST, request.FILES)
        if form.is_valid():
            cinema = form.save(commit=False)
            cinema.added_by = request.user  
            cinema.save()
            return redirect('view') 
    else:
        form = CinemaForm()
    return render(request, 'add.html', {'form': form})



def view(request):
    cinemas_list = Cinema.objects.all()
    paginator = Paginator(cinemas_list, 5) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'view.html', {'cinemas': page_obj})



def update_cinema(request, pk):
    cinema = get_object_or_404(Cinema, pk=pk)
    if request.method == 'POST':
        form = CinemaForm(request.POST, request.FILES, instance=cinema)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = CinemaForm(instance=cinema)
    
    return render(request, 'update_cinema.html', {'form': form})



def delete_cinema(request, pk):
    cinema = get_object_or_404(Cinema, pk=pk)
    
    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            cinema.delete()
            messages.success(request, 'Movie deleted successfully.')
            return redirect('view')
        else:
            return redirect('view')
    
    return render(request, 'delete_cinema.html', {'cinema': cinema})



def search_by_category(request):
    if 'category' in request.GET:
        category = request.GET['category']
        movies = Cinema.objects.filter(category__icontains=category)
        return render(request, 'movies_by_cat.html', {'category': category, 'movies': movies})
    else:
        return render(request, 'error.html', {'error_message': 'Category parameter is missing'})
    


def rate_movie(request, cinema_id):
    
    cinema = Cinema.objects.get(pk=cinema_id)
    
    if request.method == 'POST':
        return redirect('view')
    return render(request, 'rate_movie.html', {'cinema': cinema})




def comment_movie(request, cinema_id):
    cinema = Cinema.objects.get(pk=cinema_id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        return redirect('view')  
    return render(request, 'comment_movie.html', {'cinema': cinema})
