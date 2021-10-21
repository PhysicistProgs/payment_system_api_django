from django.urls import path, include

from .views import UserViewSet, CardViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api_payment_app'
router = DefaultRouter()
router.register(r'users', UserViewSet,)
router.register(r'cards', CardViewSet,)

# router.register(r'invoices', InvoiceViewSet)


urlpatterns = [
    # path('cards/', CardListView.as_view()),
    path(r'', include(router.urls))
    # path('users/', UserListView.as_view())
]
