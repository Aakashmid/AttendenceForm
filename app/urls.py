from django.contrib import admin
from django.urls import path
from .import views

app_name='app'
urlpatterns = [
    path('',views.home,name='Home'),
    path('<int:condidate_id>',views.home,name='Home'),
    path('login-user/',views.loginhand,name='Login'),
    path('logout-user/',views.logouthand,name='Logout'),
    path('create-user/<str:username>/<str:password>',views.createuser,name='Create Account'),
]