from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'mysite'
urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('home/', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('conformation/', views.conformation, name='conformation'),
    path('profiles/', views.profiles, name='profiles'),
    path('search_labourers/', views.search_labourers, name='search_labourers'),
    path('job/', views.job, name='job'),
    path('add_application_form_submission/', views.add_application_form_submission, name='add_application_form_submission'),
    path('hire_submission/', views.hire_submission, name='hire_submission')
    ]
