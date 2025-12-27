from django.db import models
from django.core.validators import MinValueValidator


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)
    allows_installments = models.BooleanField(default=False)
    max_installments = models.PositiveIntegerField(default=1)
    term_days = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )