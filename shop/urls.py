from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='Index'),
    path('about/', views.about,name='AboutUs'),
    path('contact/', views.contactUs,name='ContactUs'),
    path('tracker/', views.tracker,name='TrackingStatus'),
    path('cart/', views.viewCart,name='ViewCart'),
    path('search/', views.search,name='Search'),
    path('productview/<int:myid>', views.prodView,name='ProductView'),
    path('checkout/', views.checkout,name='Checkout'),
]