from django.urls import include, path

from . import views

app_name = 'antlrtt_app'
urlpatterns = [
    path('', views.home, name='index'),
    path('download-json/', views.download_json, name='download_json'),
]
