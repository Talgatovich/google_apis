from pprint import pprint

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = "test-python-380613-72d95986c57a.json"
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
	range="A1:D10",
	majorDimension="ROWS"
).execute()
pprint(values)

