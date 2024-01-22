from django.urls import path
# from acApp import views
# from acApp.views import *
# from acApp.views import home, index,userinfo, user_login,user_logout,Register,update_user,user_details
from acApp.views import *
app_name = "acApp"

urlpatterns = [
    path("home/", home, name="home_view"),
    path("index/",  index, name="index"),
    path('userinfo/', userinfo, name="userinfo"),
    path('user_login/',user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('register/', Register, name="register"),
    path('update_info/', update_user, name="update"),
    path('user_details/', user_details, name="user_details"),
    path('user_delete/<str:email>/', user_delete, name="user_delete"),


]