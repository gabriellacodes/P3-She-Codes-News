from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateAccountView(CreateView):
        form_class = CustomUserCreationForm
        success_url = reverse_lazy('login')
        template_name = 'users/createAccount.html'

class DetailAccountView(LoginRequiredMixin, generic.DetailView):
        template_name = 'users/userPage.html'
        # assigns what model will be user to display the information, e.g. which data will be displayed
        model = CustomUser
        context_object_name = 'user'
        # next line will help show the username in the URL field in the browser
        slug_field = 'username'
