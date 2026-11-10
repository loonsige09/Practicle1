from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/contacts/', views.contacts, name='contacts'),
    path('about/location/', views.location, name='location'),
    path('catalog/', views.catalog, name='catalog'),
    path('promotions/', views.promotions, name='promotions'),
]
