from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.landing_page,name='landing-page'),
    path('signin/',views.loginUser, name = 'login'),
    path('auth/',views.auth_type,name = 'register'),
    path('seller_register/', views.seller_register, name = 'seller-register'),
    path('buyer_register/',views.buyer_register,name = 'buyer-register'),
    path('logout/',views.logoutUser,name = 'logout'),
]
