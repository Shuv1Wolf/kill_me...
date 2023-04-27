from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('ok/', views.ok, name='ok'),
    path('ok/check/', views.check, name='check'),
]
