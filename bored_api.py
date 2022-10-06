import requests,json
from colorama import Fore, Style, init

init()

class Bored():
    def __init__(self):
        self.min_price = 0
        self.max_price = 0

    def find_activity():
        min_price = input("What is you minimum price?")
        max_price = input("What is you maximum price?")
        response = requests.get(f'http://www.boredapi.com/api/activity?minprice=:{min_price}&maxprice=:{max_price}-')
        print(Fore.BLUE, response["activity"])
        print(Fore.RED, response["type"])
        print(Fore.YELLOW, response["participants"])
        print(Fore.GREEN, response["price"])

