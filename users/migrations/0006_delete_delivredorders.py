# Generated by Django 4.1.7 on 2023-06-13 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DelivredOrders',
        ),
    ]
