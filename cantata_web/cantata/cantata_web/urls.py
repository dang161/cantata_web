from django.urls import path
from . import views
app_name = 'cantata_web'
urlpatterns = [
    path('', views.index, name="index"),

]