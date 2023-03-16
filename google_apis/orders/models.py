from django.db import models


class Order(models.Model):
	order_number = models.PositiveIntegerField("Номер заказа")
	price_usd = models.PositiveIntegerField("Стоимость в $")
	price_rub = models.PositiveIntegerField("Стоимость в Rub", null=True)
	delivery_time = models.CharField("Срок поставки", max_length=10)

	def __str__(self):
		a = str(self.order_number)
		return a

	def get_full_info(self):
		return f" {self.id},   {self.order_number},   {self.price},   {self.delivery_time}"
