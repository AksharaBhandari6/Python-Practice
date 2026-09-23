from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('menu/',views.menu,name="menu"),
    path('contact/',views.contact,name="contact"),
    path('reviews/',views.reviews,name="reviews")
    
]