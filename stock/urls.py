from django.urls import path
from . import views

urlpatterns = [
    path('', views.listproduits),
    path('listproduits/', views.listproduits, name='1'),
    path('addproduits/', views.addproduits, name='2'),
    path('updateproduits/', views.updateproduits, name='3'),
    path('deleteproduits/', views.deleteproduits, name='4'),
]