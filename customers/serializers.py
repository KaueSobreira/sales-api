from rest_framework import serializers
from .models import Client, PhysicalPerson, LegalPerson


class PhysicalPersonSerializer(serializers.ModelSerializer):


    class Meta:
        model = PhysicalPerson
        fields = '__all__'

class LegalPersonSerializer(serializers.ModelSerializer):


    class Meta:
        model = LegalPerson
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    physical_person = PhysicalPersonSerializer(required=False)
    legal_person = LegalPersonSerializer(required=False)


    class Meta:
        model = Client
        fields = '__all__'

    def validate_type(self, value, data):
        if value == "PF" and not data.get("physical_person"):
            raise serializers.ValidationError(
                {"physical_person": "Dados de pessoa física são obrigatórios"}
            )

        if value == "PJ" and not data.get("legal_person"):
            raise serializers.ValidationError(
                {"legal_person": "Dados de pessoa jurídica são obrigatórios"}
            )

        return value