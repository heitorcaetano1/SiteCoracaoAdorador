from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-nos/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
    path('privacidade/', views.privacidade, name='privacidade'),
    path('terms', views.terms, name='terms')
]