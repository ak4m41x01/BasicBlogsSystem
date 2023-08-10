from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profie"),
    path("profile_edit/", views.profile_edit, name="profie_edit"),
]
