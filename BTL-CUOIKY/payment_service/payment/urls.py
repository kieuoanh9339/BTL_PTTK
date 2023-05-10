from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('initiate_payment/', views.get_payment, name='initiate_payment'),
    path('payment_status/', views.user_transaction_info, name='user_transaction_info'),
    # path('payment_info/', views.user_payment_info, name='user_payment_info'),
]