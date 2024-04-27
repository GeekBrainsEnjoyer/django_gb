from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path(route='', view=include('hwapp.urls')),
    path('client_orders/', include('hwapp3.urls')),
    path(route='product_form/', view=include('hwapp4.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
