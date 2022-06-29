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
    
    # now we've collected the data from the user, we need to check 
    # it is valid before running the rest of the program to do this 
    # we need to convert our string value into a list of values, 
    # each separated by a comma

    # the split(',') removes the commas from the input string
    # there will still be commas between each 'number' when printed
    # as it is a list
    sales_data = data_str.split(',')
    
    # calls the validate_data function within get_sales_data
    validate_data(sales_data)

# the program relies on the data being six numbers
# this function will validate our data before allowing the rest of the
# program to continue
# it is passed the paramater of values, which will be the sales data list

# print(values) prints the same list as when we added print(sales_data)
# underneath the sales_data variable
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises customised ValueError if strings cannot be converted into 
    lists, or if there aren't exactly 6 values
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required. You provided {len(values)}"
            )        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")

    # ^^ the ValueError class in the except part contains the details of the
    # error triggered by the code in our try statement
    # 'as' keyword assigns ValueError object to the 'e' variable, which is
    # standard Python shorthand for 'error'

get_sales_data()