from django.db import transaction
from rest_framework import serializers
from .models import Order, OrderItem, InstallmentOrder
from products.models import Products


class OrderItemCreateSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = OrderItem
        fields = [
            "product",
            "quantity",
            "unit_price",
        ]


class InstallmentOrderCreateSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = InstallmentOrder
        fields = [
            "number",
            "amount",
            "due_date",
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True)
    installments = InstallmentOrderCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "client",
            "payment_method",
            "items",
            "installments",
        ]

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("O pedido deve ter ao menos um item")
        return value

    def validate(self, data):
        with transaction.atomic():
            for item in data["items"]:
                product = Products.objects.select_for_update().get(
                    id=item["product"].id
                )

                if product.stock < item["quantity"]:
                    raise serializers.ValidationError(
                        f"Estoque insuficiente para {product.name}"
                    )

        return data

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        installments_data = validated_data.pop("installments")

        with transaction.atomic():
            order = Order.objects.create(**validated_data, total_value=0)

            total = 0
            for item in items_data:
                total_item = item["quantity"] * item["unit_price"]
                OrderItem.objects.create(
                    order=order,
                    total_price=total_item,
                    **item
                )
                total += total_item

            order.total_value = total
            order.save()

            for installment in installments_data:
                InstallmentOrder.objects.create(
                    order=order,
                    **installment
                )

        return order