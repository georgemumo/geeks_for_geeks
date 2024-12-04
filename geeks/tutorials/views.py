from django.shortcuts import render
from django.views.generic import TemplateView
from . models import post

class HomePageView(TemplateView):
    models = post
    template_name = 'home.html'
# Create your views here.
