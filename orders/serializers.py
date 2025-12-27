from django.db import transaction
from rest_framework import serializers
from decimal import Decimal
from datetime import timedelta
from django.utils import timezone
from .models import Order, OrderItem, InstallmentOrder
from products.models import Products
from customers.serializers import ClientSerializerBFF
from payment_method.serializers import PaymentMethodSerializerBFF


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            "product",
            "quantity",
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "product_name",
            "quantity",
            "unit_price",
            "total_price",
        ]


class InstallmentOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentOrder
        fields = [
            "number",
            "amount",
            "due_date",
            "paid_at",
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True)
    installments_qty = serializers.IntegerField(required=False, min_value=1)

    class Meta:
        model = Order
        fields = [
            "client",
            "payment_method",
            "items",
            "installments_qty",
        ]

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("O pedido deve conter ao menos um item")
        return value

    def validate(self, data):
        payment_method = data["payment_method"]
        qty = data.get("installments_qty", 1)

        if payment_method.max_installments <= 1 and qty > 1:
            raise serializers.ValidationError(
                {"installments_qty": "Esta forma de pagamento não permite parcelamento"}
            )

        if qty > payment_method.max_installments:
            raise serializers.ValidationError(
                {
                    "installments_qty": f"Máximo permitido: {payment_method.max_installments} parcelas"
                }
            )

        with transaction.atomic():
            for item in data["items"]:
                product = Products.objects.select_for_update().get(
                    pk=item["product"].id
                )

                if product.stock < item["quantity"]:
                    raise serializers.ValidationError(
                        f"Estoque insuficiente para {product.name}"
                    )

        return data


    def create(self, validated_data):
        items_data = validated_data.pop("items")
        installments_qty = validated_data.pop("installments_qty", 1)
        payment_method = validated_data["payment_method"]

        with transaction.atomic():
            order = Order.objects.create(
                **validated_data,
                total_value=Decimal("0.00")
            )

            total = Decimal("0.00")

            for item in items_data:
                product = item["product"]
                unit_price = product.price
                total_item = unit_price * item["quantity"]

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item["quantity"],
                    unit_price=unit_price,
                    total_price=total_item,
                )

                total += total_item

            order.total_value = total
            order.save()

            installment_value = (total / installments_qty).quantize(Decimal("0.01"))

            for i in range(1, installments_qty + 1):
                InstallmentOrder.objects.create(
                    order=order,
                    number=i,
                    amount=installment_value,
                    due_date=timezone.now().date()
                    + timedelta(days=payment_method.term_days * i),
                )

        return order


class OrderSerializerDetail(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    installments = InstallmentOrderSerializer(many=True, read_only=True)
    client = ClientSerializerBFF()
    payment_method = PaymentMethodSerializerBFF()

    class Meta:
        model = Order
        fields = [
            "public_id",
            "situation",
            "client",
            "items",
            "total_value",
            "payment_method",
            "installments",
            "created_at",
        ]

class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializerBFF()
    payment_method = PaymentMethodSerializerBFF()

    class Meta:
        model = Order
        fields = [
            "public_id",
            "situation",
            "client",
            "total_value",
            "payment_method",
            "created_at",
        ]


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["situation"]
