from django.contrib import admin
from django.urls import path
from Quiz_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('ans/',views.answer, name="ans")
]