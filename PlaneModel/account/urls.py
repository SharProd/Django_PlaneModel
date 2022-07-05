from django.urls import path
from .views import user_login, register, user_logout

urlpatterns = [
    path('login/',user_login,name = 'login'),
    path('register/', register, name='register'),
    path('exit/', user_logout, name='exit'),
]