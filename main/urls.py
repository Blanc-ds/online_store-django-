from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from main import views

from app import settings

app_name = 'main'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('payment/', views.about, name='payment'),
    path('contacts/', views.about, name='contacts'),

]
