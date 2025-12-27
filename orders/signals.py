from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import OrderItem, Order


@receiver(post_save, sender=OrderItem)
def decrease_stock_on_order_item_create(sender, instance, created, **kwargs):
    if not created:
        return

    product = instance.product
    product.stock -= instance.quantity
    product.save()

@receiver(pre_save, sender=Order)
def restore_stock_on_cancel(sender, instance, **kwargs):
    if not instance.pk:
        return

    old_order = Order.objects.get(pk=instance.pk)

    if old_order.situation != 'CANCELADA' and instance.situation == 'CANCELADA':
        for item in instance.items.all():
            product = item.product
            product.stock += item.quantity
            product.save()