
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home ,name="home"),
    path('about/', views.about,name="about"),
    path('service/', views.service ,name="service"),
    path('menu/', views.menu ,name="menu"),
    path('reservation/', views.reservation_p ,name="reservation"),
    path('contact/', views.contact, name="contact"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('gallery/', views.gallery, name="gallery")
]

