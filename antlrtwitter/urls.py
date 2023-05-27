from django.urls import path
from . import views

app_name = 'antlrtwitter'

urlpatterns = [
    path('', views.home, name='index')
]