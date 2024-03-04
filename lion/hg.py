import datetime
import sys
import threading
import time
from os import system, name

expirydate = datetime.date(2021, 9, 24)
# expirydate = datetime.date(2021, 8, 30)
today = datetime.date.today()

def hero():
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux (here, os.name is 'posix')
        else:
            _ = system('clear')
            
    def getSum(n):
        total = 0
        for digit in str(n):
            total += int(digit)
        return total
    
    clear()
    y = 1
    newperiod = 0  # Initialize newperiod
    banner = 'figlet RXCEV2.1|lolcat'
    numbers = []
    
    while y:
        clear()
        system(banner)
        print(f"Contact me on telegram @smsn_knt")
        print(f"Enter {newperiod} Bcone Price :")
        current = input()
        current = int(current)
        print("\n---------Successfully hacked the server-----------")
        print("\n---------Successfully got the colour -------------")
        print('\n')
        
        last2 = str(current)[-2:]
        if newperiod % 2 == 0:
            total = getSum(current)
            if total % 2 == 0:
                print(f"{newperiod + 1} : 🔴,RED ")
            else:
                print(f"{newperiod + 1} : 💚,GREEN ")  # Use the correct GREEN emoji
        else:
            total = getSum(current)
            if total % 2 == 0:
                print(f"{newperiod + 1} : 🔴,RED ")
            else:
                print(f"{newperiod + 1} : 💚,GREEN ")  # Use the correct GREEN emoji
        
        newperiod += 1
        numbers.append(current)
        y = int(input("Do you want to play? Press 1 to continue or 0 to exit: \n"))
        
        if y == 0:
            y = False
        
        if len(numbers) > 19:
            clear()
            system('figlet Thank you!!')
            print("Play on the next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @smsn_knt")

if expirydate > today:
    now = datetime.datetime.now()
    First = now.replace(hour=13, minute=55, second=0, microsecond=0)

hero()
