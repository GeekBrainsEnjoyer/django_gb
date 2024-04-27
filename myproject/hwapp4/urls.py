from django.urls import path
from . import views

app_name = 'hwapp4'

urlpatterns = [
    path('', views.product_form, name='product_form'),

]
