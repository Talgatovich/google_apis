from pprint import pprint

import gspread
# Указываем путь к JSON
gc = gspread.service_account(filename='../orders/cred_google.json')
#Открываем тестовую таблицу
sh = gc.open("Test")
#Выводим значение ячейки A1

pprint(sh.values_get(range='A1:D10'))