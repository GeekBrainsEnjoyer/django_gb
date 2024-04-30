from django.urls import path
from . import views

app_name = 'hwapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:client_pk>/', views.client_orders, name='client_orders'),
    path('<int:client_pk>/<int:days>/', views.client_orders_by_date,
         name='client_orders_by_date'),
    path('product_form/', views.product_form, name='product_form'),
]
