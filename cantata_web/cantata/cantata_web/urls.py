from django.urls import path
from . import views
app_name = 'cantata_web'
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),

]