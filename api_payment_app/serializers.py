from django.contrib.auth.models import User
from rest_framework import serializers

from api_payment_app.models import PaymentCard, Invoice


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'is_active']
        read_only_fields = ['is_active']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CardSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name="api:user-detail", read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="api:paymentcard-detail", read_only=True)

    class Meta:
        model = PaymentCard
        fields = ['url', 'number', 'balance', 'owner']
        read_only_fields = ['balance', 'owner']


class CardUpdateSerializer(serializers.ModelSerializer):
    added_amount = serializers.IntegerField(write_only=True)
    owner = serializers.HyperlinkedRelatedField(view_name="api:user-detail", read_only=True)

    class Meta:
        model = PaymentCard
        fields = ['number', 'balance', 'owner', 'added_amount']
        read_only_fields = ['balance', 'owner', 'number']

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.balance += validated_data['added_amount']
        instance.save()
        return instance


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['amount', 'card', 'is_payed']
        read_only_fields = ['card', 'is_payed']
