from django.contrib.auth.models import User
from django.db import models


class PaymentCard(models.Model):
    number = models.BigIntegerField(unique=True)
    balance = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Invoice(models.Model):
    amount = models.IntegerField()
    is_payed = models.BooleanField(default=False, )


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.IntegerField()
    card = models.ForeignKey(PaymentCard, on_delete=models.CASCADE, null=False)


