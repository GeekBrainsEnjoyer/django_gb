from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('client_orders/', include('hwapp3.urls')),
    path(route='', view=include('hwapp.urls')),
]
