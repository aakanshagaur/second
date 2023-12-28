from django.contrib import admin
from django.urls import path
from . import views
from django.views import View

urlpatterns = [
    path("admin/", admin.site.urls),
    path ("", views.index), 
    path ("about/", views.about), 
    path ("blog/", views.blog),
    path ("gallery/", views.gallery),
    path ("service/", views.service),
    path("contact/", views.contact),

    path('AfterContact/', views.AfterContact.as_view())
]