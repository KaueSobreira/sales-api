import uuid
from django.db import models
from customers.models import Client
from products.models import Products
from payment_method.models import PaymentMethod


STATUS_CHOICES = (
    ('REALIZADA', 'Realizada'),
    ('CANCELADA', 'Cancelada'),
)

class Order(models.Model):
    public_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    situation = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='REALIZADA'
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name='orders'
    )

    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.PROTECT,
        related_name='orders'
    )

    total_value = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Products,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

class InstallmentOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='installments'
    )

    number = models.PositiveIntegerField()
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    due_date = models.DateField()
    paid_at = models.DateTimeField(null=True, blank=True)
