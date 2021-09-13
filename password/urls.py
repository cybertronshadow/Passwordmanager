from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register', views.registeruser, name='register'),
    path('storedpassword/', views.storedpassword, name='storedpassword'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]
