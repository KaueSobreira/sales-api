from django.db import models


TYPES_OF_PEOPLE = (
    ('PF', 'Pessoa Física'),
    ('PJ', 'Pessoa Jurídica'),
)

class Client(models.Model):
    type = models.CharField(
        max_length=2,
        choices=TYPES_OF_PEOPLE,
    )
    phone = models.CharField(max_length=20, blank=True, null=True)

class PhysicalPerson(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField(blank=True, null=True)

class LegalPerson(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    trade_name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)
