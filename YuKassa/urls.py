from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    #path('1/', views.payment1, name='payment1')
]
