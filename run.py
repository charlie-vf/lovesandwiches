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

# collect sales data from user
def get_sales_data():
    """
    Get sales figures input from the user
    """
    print('Please enter sales data from the last market.')
    print('Data should be six numbers, separated by commas.')
    print('Example: 10, 20, 25, 17, 25, 30\n')

    # use input() method to get sales data from user in terminal
    # will be returned as a string
    data_str = input('Enter your data here: ')
    print(f'The data provided is {data_str}')

get_sales_data()