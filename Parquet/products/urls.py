from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('massiv/', views.massiv, name='massiv'),
    path('contact/', views.contact, name='contact'),
    path('shpon/', views.shpon, name='shpon'),
    path('callback/', views.order, name='callback'),
]