from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path('register/login/', views.Register_Login_View.as_view(), name="register_login"),
    path('otpcode/', views.CzechOtpView.as_view(), name="check_otp"),
    path('panel/', views.PanelUser.as_view(), name="panel_user"),
    path('panelcreate/', views.PanelCreateUser.as_view(), name="panel_create"),
    path('panelupdate/<int:pk>', views.PanelUpdateUser.as_view(), name="panel_update"),
    path('profile/user/<int:pk>', views.ProfileUser.as_view(), name="profile"),
    path('author/about/<int:pk>', views.author_about.as_view(), name="author"),
    path('logout/', views.user_logout, name='logout'),
]