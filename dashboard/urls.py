from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('payment/', views.payment, name='payment'),
    path('ticket/', views.ticket, name='ticket'),
    path('money_req/', views.money_req, name='money_req'),
    path('to-bank/<int:order_id>/', views.to_bank, name='to_bank'),
    path('callback/', views.callback, name='callback'),
]
