from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="HomePage"),
    path('about/',views.about,name="AboutPage"),
    path('menu/',views.menu,name="Menu"),
    path('contact/',views.contact,name="ContactUs"),
    path('reviews/',views.reviews,name="Reviews")
    
]