from rest_framework import serializers
from django.db import transaction
from .models import Client, PhysicalPerson, LegalPerson


class PhysicalPersonSerializer(serializers.ModelSerializer):


    class Meta:
        model = PhysicalPerson
        fields = ['id', 'full_name', 'cpf', 'birth_date']

class LegalPersonSerializer(serializers.ModelSerializer):


    class Meta:
        model = LegalPerson
        fields = ['id', 'company_name', 'trade_name', 'cnpj']

class ClientSerializer(serializers.ModelSerializer):
    physical_person = PhysicalPersonSerializer(required=False)
    legal_person = LegalPersonSerializer(required=False)


    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        client_type = data.get("type")

        if not client_type:
            raise serializers.ValidationError(
                {"type": "O tipo de cliente é obrigatório"}
            )
        if data["type"] == "PF" and not data.get("physical_person"):
            raise serializers.ValidationError(
                {"physical_person": "Dados de pessoa física são obrigatórios"}
            )

        if data["type"] == "PJ" and not data.get("legal_person"):
            raise serializers.ValidationError(
                {"legal_person": "Dados de pessoa jurídica são obrigatórios"}
            )

        return data

    @transaction.atomic
    def create(self, validated_data):
        physical_data = validated_data.pop("physical_person", None)
        legal_data = validated_data.pop("legal_person", None)

        client = Client.objects.create(**validated_data)

        if client.type == "PF":
            PhysicalPerson.objects.create(client=client, **physical_data)

        if client.type == "PJ":
            LegalPerson.objects.create(client=client, **legal_data)

        return client

    @transaction.atomic
    def update(self, instance, validated_data):
        physical_data = validated_data.pop("physical_person", None)
        legal_data = validated_data.pop("legal_person", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if instance.type == "PF" and physical_data:
            PhysicalPerson.objects.update_or_create(
                client=instance,
                defaults=physical_data
            )

        if instance.type == "PJ" and legal_data:
            LegalPerson.objects.update_or_create(
                client=instance,
                defaults=legal_data
            )

        return instance

class ClientSerializerBFF(serializers.ModelSerializer):
    physical_person = PhysicalPersonSerializer(read_only=True)
    legal_person = LegalPersonSerializer(read_only=True)


    class Meta:
        model = Client
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.type == 'PF':
            data.pop("legal_person", None)
        elif instance.type == 'PJ':
            data.pop("physical_person", None)

        return data