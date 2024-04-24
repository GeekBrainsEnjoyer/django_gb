from django.urls import path
from . import views

app_name = 'hwapp3'

urlpatterns = [
    path('<int:client_pk>/', views.client_orders, name='client_orders'),
    path('<int:client_pk>/<int:days>/', views.client_orders_by_date,
         name='client_orders_by_date'),
]
