# Generated by Django 4.2.16 on 2024-10-08 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_event_category_alter_event_payment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Music', 'Music'), ('Sports', 'Sports'), ('Theatre', 'Theatre'), ('Dance', 'Dance')], max_length=50),
        ),
    ]
