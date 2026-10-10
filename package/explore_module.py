from datetime import datetime
import time
import math
import random
from uuid import uuid4

def explore_module():
    while True:
        print("Select Opeation")
        print("1. Datetime and Time Operations")
        print("2. Mathematicl Operations")
        print("3. Random operator")
        print("4. Generate UUID")
        print("5. Exit")

        choice = int(input("Enter your choice number (1-5)"))

        if choice == 1:
            print(dir(datetime))
            print(dir(time))

        elif choice == 2:    
            print(dir(math))

        elif choice == 3:
            print(dir(random))

        elif choice == 4:
            print(dir(uuid4))

        elif choice == 5:
            break

        else:
            print("Invalid Choice")                