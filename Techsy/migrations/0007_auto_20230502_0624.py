# Generated by Django 3.2.18 on 2023-05-02 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Techsy', '0006_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]