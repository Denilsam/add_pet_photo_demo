from django.urls import path
from .views import (PetListView, PetCreateView, PetUpdateView, PetDeleteView,
                    UserLoginView, UserLogoutView, UserRegisterView)

urlpatterns = [
    path('', PetListView.as_view(), name='pet_list'),
    path('add/', PetCreateView.as_view(), name='pet_add'),
    path('edit/<int:pk>/', PetUpdateView.as_view(), name='pet_edit'),
    path('delete/<int:pk>/', PetDeleteView.as_view(), name='pet_delete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]