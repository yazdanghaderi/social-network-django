from django.urls import path
from . import views
app_name = "account:"
urlpatterns = [
    path("register/", views.UserRegisteraion.as_view(), name='user_register' ),
    path("login/", views.UserLogin.as_view(), name='user_login' ),
    path("logout/", views.UserLogout.as_view(), name='user_logout' ),
    path("profile/<int:pid>", views.UserProfileView.as_view(), name='user_profile' ),
]