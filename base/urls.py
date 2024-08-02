from django.urls import path
from .views import bfhl, frontend

urlpatterns = [
    path('bfhl', bfhl, name='bfhl'),
    path('', frontend, name='frontend'),
]