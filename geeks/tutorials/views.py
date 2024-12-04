from django.contrib import auth
from django.views.generic import TemplateView
from . models import post
from geeks.templates.forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


class HomePageView(TemplateView):
    models = post
    template_name = 'home.html'
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('home.html')
            d = {'username': username, }
            subject, from_email, to = 'welcome', 'your_email@gmail.com',email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, 'Thank you for registering! You are now able to login')
            return redirect('login')
        else:
            form = UserRegisterForm()
            return render(request, 'registration/register.html', {'form': form})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Create account first')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})