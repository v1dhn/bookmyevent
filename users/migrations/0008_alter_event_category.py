# Generated by Django 4.2.16 on 2024-10-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_event_location_alter_event_payment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('music', 'Music'), ('sports', 'Sports'), ('theatre', 'Theatre'), ('dance', 'Dance')], max_length=50),
        ),
    ]