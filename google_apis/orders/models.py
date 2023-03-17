from django.db import models


class Order(models.Model):
    """Заказы"""
    order_number = models.PositiveIntegerField("Номер заказа")
    price_usd = models.PositiveIntegerField("Стоимость в $")
    price_rub = models.PositiveIntegerField("Стоимость в Rub", null=True)
    delivery_time = models.CharField("Срок поставки", max_length=10)

    def __str__(self):
        return f"{self.order_number}"
