# Generated by Django 4.1.7 on 2023-03-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="delivery_time",
            field=models.CharField(max_length=10, verbose_name="Срок поставки"),
        ),
    ]
