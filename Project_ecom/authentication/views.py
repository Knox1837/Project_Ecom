from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Class based view

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Sucessful!")
            return redirect('product_index')
        
        return redirect('login')

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    def post(self, request):
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        send_mail(
            'Account Creation Sucessful!', # subject
            'Thank you for registering.\n Username: '+ user.username +'\nName:'+user.first_name + "\n" + user.last_name+'\nEmail: '+ user.email, # body
            'kaustuvm1837@gmail.com', # sender
            [user.email] # receiver        -sent to(CC): written in a list
        )
        return redirect('login')
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logout Sucessful!")
        return redirect('login')
