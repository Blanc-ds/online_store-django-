from django.urls import path
from django.conf.urls.static import static


from users import views

from app import settings

app_name = "users"


urlpatterns = [
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
    
]
