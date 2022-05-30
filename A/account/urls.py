from django.urls import path
from . import views
app_name = "account:"
urlpatterns = [
    path("register/", views.UserRegisteraion.as_view(), name='user_register' ),
    path("login/", views.UserLogin.as_view(), name='user_login' ),
    path("logout/", views.UserLogout.as_view(), name='user_logout' ),
    path("profile/<int:pid>", views.UserProfileView.as_view(), name='user_profile' ),
    path("reset/", views.UserPasswordResetView.as_view(), name='reset_pasword'),
    path("reset/done/", views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path("confirm/<uidb64>/<token>/", views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("confirm/", views.UserPassowrdResetCompleteView.as_view(), name='password_reset_complete'),
    path("follow/<int:user_id>/", views.UserFollowView.as_view(), name='user_follow'),
    path("unfollow/<int:user_id>/", views.UserUnfollowView.as_view(), name='user_unfollow'),
    path("edit_user/", views.EditUserView.as_view(), name='edit_user'),
]