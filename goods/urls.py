from django.urls import path
from django.conf.urls.static import static


from goods import views

from app import settings

app_name = "goods"


urlpatterns = [
    path("<slug:category_slug>", views.catalog, name="index"),
    path("<slug:category_slug>/<int:page>/", views.catalog, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
