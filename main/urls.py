from django.urls import path

from main.decorators import check_recaptcha
from main import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('bouquets/', views.bouquets, name='bouquets_url'),
    path('slider/', views.slider, name='slider_url'),
    path('bouquets_nevest/', views.bouquets_nevest, name='bouquets_nevest_url'),
    path('compositions/', views.compositions, name='compositions_url'),
    path('register/', check_recaptcha(views.RegisterView.as_view()), name='register'),
    path('contact/', views.contact, name='contact_url'),
]
