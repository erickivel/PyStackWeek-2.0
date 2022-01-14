from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="signUp"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
