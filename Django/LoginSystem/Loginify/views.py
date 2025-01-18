from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UserDetails

# Testing View
def test_view(request):
    return HttpResponse("Hello, world!")

# Signup View
# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         if not UserDetails.objects.filter(email=email).exists():
#             UserDetails.objects.create(username=username, email=email, password=password)
#             return redirect('login')
#         else:
#             return HttpResponse("Email already exists.")
#     return render(request, 'signup.html')
def signup_view(request):
    print("Trying to render signup.html")  # Debugging
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not UserDetails.objects.filter(email=email).exists():
            UserDetails.objects.create(username=username, email=email, password=password)
            return redirect('login')
        else:
            return HttpResponse("Email already exists.")
    return render(request, 'signup.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = UserDetails.objects.filter(email=email, password=password).first()
        if user:
            return HttpResponse(f"Welcome, {user.username}!")
        else:
            return HttpResponse("Invalid credentials.")
    return render(request, 'login.html')

# CRUD Views
def get_all_users(request):
    users = UserDetails.objects.all()
    return render(request, 'users_list.html', {'users': users})

def get_user_by_email(request, email):
    user = get_object_or_404(UserDetails, email=email)
    return render(request, 'user_detail.html', {'user': user})

def update_user(request, email):
    user = get_object_or_404(UserDetails, email=email)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.save()
        return redirect('users_list')
    return render(request, 'update_user.html', {'user': user})

def delete_user(request, email):
    user = get_object_or_404(UserDetails, email=email)
    if request.method == 'POST':
        user.delete()
        return redirect('users_list')
    return render(request, 'delete_confirm.html', {'user': user})
