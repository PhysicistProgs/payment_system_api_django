from django.contrib.auth.models import User
from rest_framework import viewsets
from api_payment_app.models import PaymentCard, Invoice
from api_payment_app.serializers import CardSerializer, InvoiceSerializer, UserSerializer, CardUpdateSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = PaymentCard.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    serializers = {
        'default': CardSerializer,
        'update': CardUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action,
                                    self.serializers['default'])


class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer



class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
