# Generated by Django 4.2.16 on 2024-10-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
