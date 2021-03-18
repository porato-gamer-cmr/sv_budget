from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<id_produit>', views.detail, name='detail'),
    path('save/', views.save_product, name='save_product'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('produits/',views.produits, name='produits'),
    path('approv/',views.approv, name='approv'),
    path('reapprov/',views.reapprov, name='reapprov')
]