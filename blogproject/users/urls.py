#from django.contrib import admin
from django.urls import path , include
from . import views
#from django.views import View

urlpatterns = [

    path("", views.index),
    path("about/", views.about),
    path("blog/", views.blog),
    path("contact/", views.contact),
    path("signup/", views.signup),
    path("login/", views.login),

    path("aftersignup/", views.AfterSignup.as_view()),
    path("afterlogin/", views.Afterlogin.as_view()),
    path("checkotp/",views.Checkotp.as_view()),
    path("logout/",views.logout),

    
    #path("", include("users.urls"))
    
]
