from django.urls import path
from django.conf.urls.static import static
from goods import views

from app import settings

app_name = 'goods'


urlpatterns = [
    path('', views.catalog , name='index'),
    path('product/', views.product, name='product'),
   

]
