# a djang url file for the dummy app
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]
