from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('bouquets/', views.bouquets, name='bouquets_url'),
    path('slider/', views.slider, name='slider_url'),
]
