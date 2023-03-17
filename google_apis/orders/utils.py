from xml.etree import ElementTree as ET
import requests
import datetime

CURRENT_DATE = datetime.datetime.now()


def get_current_rate():
    """Получение текущего курса доллара"""
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url=url)
    course = (
        ET.fromstring(response.text)
        .find("./Valute[CharCode='USD']/Value")
        .text.replace(",", ".")
    )
    return float(course)


def check_db(data, model):
    queryset = model.objects.all()
    black_list = []
    new_data = [int(val[1]) for val in data if len(val) != 0]
    for value in queryset:
        if value.order_number not in new_data:
            black_list.append(value.order_number)
    queryset.filter(order_number__in=black_list).delete()


def check_for_updates(val, model):
    """Проверка заказа на наличие обновлений"""
    order = model.objects.get(order_number=val[1])
    if order.price_usd != val[2]:
        order.price_usd = val[2]
    if order.delivery_time != val[3]:
        order.delivery_time = val[3]
    order.save()


def check_delivery_time(queryset):
    """Проверка просроченных заказов"""
    result = []
    for obj in queryset:
        obj_date = datetime.datetime.strptime(obj.delivery_time, "%d.%m.%Y")
        if obj_date < CURRENT_DATE:
            result.append(int(obj.order_number))
    return result
