from django.db import models


class Order(models.Model):
	order_number = models.PositiveIntegerField("Номер заказа")
	price = models.PositiveIntegerField("Стоимость в $$")
	delivery_time = models.DateTimeField("Срок поставки")

