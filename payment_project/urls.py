
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_payment_app.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls')),
]
