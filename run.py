# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
# import Credentials as no need to import the entire google.auth library
from google.oauth2.service_account import Credentials

from pprint import pprint

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
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will request data until it is valid.
    """

    # while loop continues to request data over and over until
    # we get a valid response, rather than having to restart the
    # program each time invalid data is provided
    # this is much better user experience
    while True:
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
        # validate_data(sales_data)
        # after adding return True and return False to validate_data function,
        # this call was moved to the 'if' statement below

        # sets condition to end while loop when valid data inputed
        # use validate_data function to return either True or False value
        # depending on if the data is valid or not - return True in the
        # validate_data function
        if validate_data(sales_data):
            print('Data is valid')
            break
    
    # return validated sales_data from get_sales_data function
    return sales_data

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
        # for each individual value in the values list, convert it into
        # an integer
        [int(value) for value in values]

        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required. You provided {len(values)}"
            )        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        # if program throws errors:
        return False

    # if program runs without errors:
    return True
    # use the return value as the condition for ending the while loop in
    # get_sales_data function.

    # ^^ the ValueError class in the except part contains the details of the
    # error triggered by the code in our try statement
    # 'as' keyword assigns ValueError object to the 'e' variable, which is
    # standard Python shorthand for 'error'

# function needs to be passed the data to work
def update_sales_worksheet(data):
    """
    Update sales worksheet. Insert new row with the list data provided.
    """
    print("Updating sales worksheet...\n")
    # access sales worksheet from Google Sheet by declaring new variable so we
    # can add data to it. Assign it the SHEET variable which was given the
    # data using the gspread library at the top of the page
    # use gspread worksheet() method to access sales worksheet
    sales_worksheet = SHEET.worksheet('sales')
    # use gspread append_row method to insert data into worksheet
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


# FUNCTION CALLS BELOW - it is good practice to put all the main function calls
# into a function called main.
# REMEMBER - you cannot call a function above where it is defined, so call 'main'
# below its definition

# get_sales_data() call changed to variable data = get_sales_data() once 
# while loop & validation completed as function now returns a value 
# and we need a place to put it. aka, this contains the data from the function

# data = get_sales_data()

# list comprehension to convert data from list (['1', ' 2', ' 3', ' 4', ' 5', ' 6'])
# into integers so the spreadsheet can work with them

# sales_data = [int(num) for num in data]

# then create new function which inserts this sales_data into a new entry
# in the sales worksheet in the Google Sheet - this is the
# update_sales_worskheet function

# update_sales_worksheet(sales_data)


# function to calculate surplus data
# pass it sales data list
def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate surplus for each item.

    The surplus is defined as the sales figure subtractd from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")

    # need stock data from before market - line 9 of stock worksheet
    # use get_all_values method to get all values
    stock = SHEET.worksheet('stock').get_all_values()
    # ^^ this gets every row from the stock worksheet

    # standard list index won't work, as every time new data is added to the
    # stock worksheet, the row number we want will increase
    # use a slice - square brackets - will slice te final
    stock_row = stock[-1]
    print(stock_row)



def main():
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)


print("Welcome to Love Sandwiches data automation.\n")
main()