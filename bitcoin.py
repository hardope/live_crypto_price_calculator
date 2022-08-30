import requests
import json
import sys
import locale


amount = 0

# Inserts comma into numbers
def intWithCommas(x):
    if type(x) not in [type(0), type(0)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)

# check command line arguments
if len(sys.argv) < 2:
     sys.exit("Missing command line argument.")
elif len(sys.argv) > 2:
     sys.exit("Too many command line arguments.")
else:
     try:
          #confirms if user inputed a corect value of bitcoin
          amount = float(sys.argv[1])
     except:
          sys.exit("Command line arguement is not a number.")
     try:
          # queries api for live prices
          responce = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
          object = responce.json()

          # indexes into json object to get desired values
          price = object['bpi']['USD']['rate']
          price = price.replace(",", "")
          price = float(price) * amount
          price = str(price)
          
          a, b = price.split('.')
          a = int(a)

          # prints results of the comma function
          print(f"${intWithCommas(a)}.{b}")

          
     except:
          sys.exit("Something went wrong, Try again.")
     