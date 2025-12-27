from django.db import migrations


def create_consumidor_final(apps, schema_editor):
    Client = apps.get_model('customers', 'Client')
    PhysicalPerson = apps.get_model('customers', 'PhysicalPerson')

    client, created = Client.objects.get_or_create(
        defaults={
            'type': 'PF',
            'phone': '0000000000',
        }
    )

    if created:
        PhysicalPerson.objects.create(
            client=client,
            full_name='Consumidor Final',
            cpf='00000000000',
        )


def reverse_func(apps, schema_editor):
    Client = apps.get_model('customers', 'Client')
    PhysicalPerson = apps.get_model('customers', 'PhysicalPerson')

    PhysicalPerson.objects.filter(
        client__email='consumidor.final@sistema.local'
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_client_phone_alter_physicalperson_birth_date'),
    ]

    operations = [
        migrations.RunPython(create_consumidor_final, reverse_func),
    ]
