# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
# import Credentials as no need to import the entire google.auth library
from google.oauth2.service_account import Credentials

# Lists the APIs that the program should access in order to run
# SCOPE in capitals as it is a constant
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# call the from_service_account_file method of Credentials class
#  & pass it creds file name
CREDS = Credentials.from_service_account_file('creds.json')

# create variable using using with_scopes method of creds object
# pass it the SCOPE variable
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# access love_sandwiches google sheet by passing variable name of spreadsheet
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# ^^^ Above settings are required to access spreadsheet data

# access data in sales worksheet
sales = SHEET.worksheet('sales')

data = sales.get_all_values()
print(data)