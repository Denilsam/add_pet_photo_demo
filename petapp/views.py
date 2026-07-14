from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Petshop

class PetListView(LoginRequiredMixin, ListView):
    model = Petshop
    template_name = 'list.html'
    context_object_name = 'pets'
    login_url = 'login'

class PetCreateView(LoginRequiredMixin, CreateView):
    model = Petshop
    fields = ['pet_name', 'pet_image']
    template_name = 'add.html'
    success_url = reverse_lazy('pet_list')
    login_url = 'login'

class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Petshop
    fields = ['pet_name', 'pet_image']
    template_name = 'edit.html'
    success_url = reverse_lazy('pet_list')
    login_url = 'login'

class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Petshop
    template_name = 'delete.html'
    success_url = reverse_lazy('pet_list')
    login_url = 'login'

class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('pet_list')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
