from django.db.models import Sum
from pprint import pprint

from django.shortcuts import render
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

from orders.models import Order
from orders.utils import check_db, check_for_updates, get_current_rate

CREDENTIALS_FILE = "orders/cred_google.json"
CURRENT_RATE = get_current_rate()


def get_data_from_google_sheets():
	spreadsheet_id = "1xcqi4iruwBJA_bpqW10wxlcOJEPsGfThcxm0hxQ3EUQ"

	credentials = ServiceAccountCredentials.from_json_keyfile_name(
		CREDENTIALS_FILE,
		[
			"https://www.googleapis.com/auth/spreadsheets",
			"https://www.googleapis.com/auth/drive"
		]
	)
	http_auth = credentials.authorize(httplib2.Http())
	service = apiclient.discovery.build("sheets", "v4", http=http_auth)

	result = service.spreadsheets().values().get(
		spreadsheetId=spreadsheet_id,
		range="A2:D",
		majorDimension="ROWS"
	).execute()
	return result.get('values', [])


def data_view(request):

	data = get_data_from_google_sheets()
	for val in data:
		if len(val) == 0:
			continue
		if Order.objects.filter(order_number=val[1]).exists():
			check_for_updates(val, Order)
			continue
		else:
			Order.objects.create(
				order_number=val[1],
				price_usd=val[2],
				price_rub=int(val[2]) * CURRENT_RATE,
				delivery_time=val[3]
			)
	check_db(data, Order)
	queryset = Order.objects.all().order_by("pk")
	total = queryset.aggregate(Sum("price_rub"))

	return render(request, "index.html", {"data": queryset, "total": total})
