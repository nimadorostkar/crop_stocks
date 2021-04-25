from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #path('payment/', views.payment, name='payment'),
    path('ticket/', views.ticket, name='ticket'),
    path('money_req/', views.money_req, name='money_req'),
]
