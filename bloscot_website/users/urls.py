from django.contrib import admin
from django.urls import path, include
from . import views
from django.views import View

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("users.urls")),
    path("", views.index),
    path('about/', views.about),
    path('blog/', views.blog),
    path('contact/', views.contact),
    path('features/', views.features),
    path('login/', views.login),
    path('signup/', views.signup),


    path('aftersignup/', views.AfterSignup.as_view()),
    path('afterlogin/', views.Afterlogin.as_view()),
    path("checkotp/", views.checkotp.as_view()),
    # path("logout/", views.logout),
    path("addblog/", views.addblog)
]