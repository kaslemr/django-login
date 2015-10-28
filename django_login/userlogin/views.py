from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView
from userlogin.models import Profile


class BaseView(TemplateView):
    template_name = "base.html"

class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/create/profile/"

class CreateProfile(CreateView):
    model = Profile
    fields = ['type']
    success_url = "/"
    pass