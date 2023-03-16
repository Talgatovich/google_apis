from pprint import pprint
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

from models import Order

if __name__ == "__main__":
	CREDENTIALS_FILE = "cred_google.json"
	spreadsheet_id = "1xcqi4iruwBJA_bpqW10wxlcOJEPsGfThcxm0hxQ3EUQ"

	credentials = ServiceAccountCredentials.from_json_keyfile_name(
		CREDENTIALS_FILE,
		[
			"https://www.googleapis.com/auth/spreadsheets",
			"https://www.googleapis.com/auth/drive"
		]
	)
	httpAuth = credentials.authorize(httplib2.Http())
	service = apiclient.discovery.build("sheets", "v4", http=httpAuth)

	values = service.spreadsheets().values().get(
		spreadsheetId=spreadsheet_id,
		range="A2:D10",
		majorDimension="ROWS"
	).execute()
	# pprint(values["values"])
	res_list = []
	for val in values["values"]:
		print(val)
	order = Order(
		order_number=val[1],
		price=val[2],
		delivery_time=val[3]
	)
	res_list.append(order)
	Order.objects.bulk_create(res_list)
	print(res_list)
