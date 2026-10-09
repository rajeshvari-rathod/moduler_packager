from datetime import datetime
import time
import math
from uuid import uuid4
import random


def dt_operator():
    while True:
        print("\n Datetime and Time Operations: ")
        print("1. Display Current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into  custom format")
        print("4. stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = int(input("Enter your choice number (1-6):"))

        if choice == 1:
            print(datetime.now())
        
        elif choice == 2:
            first1 = input("Enter the First Date")
            second2 = input("Enter the Second Date")

            first1 = datetime.strptime(first1,"%Y/%m/%d")
            second2 = datetime.strptime(second2,"%Y/%m/%d")

            new_dt = abs(second2 - first1)
            print(f"Difference between two date is: {new_dt}")

        elif choice == 3:
            current_dt = datetime.now()
            print("1. for date")
            print("2. for time")
            print("3. for both")

            num = int(input("Entery your choice number: "))

            if num == 1:
                print(current_dt.strftime("%y/%m/%d"))

            elif num == 2:
                print(current_dt.strftime("%H:%M:%S"))

            else:
                print("Invalid choice number")        

        elif choice == 4:
            start = time.time()
            stop = input("entery the stop time")
            end = time.time()
            print(f"stopwatch difference time{end - start}")

        elif choice == 5:
            num = int(input("enter the countdown Timer"))
            while num > 0:
                time.sleep(1)
                num=(-1)
                
        elif choice == 6:
              break
        else:
            print("Invalid choice number")


def math_operator():  
                          
        while True:
            print("================================")
            print("Mathematical Operations:")
            print("1. Calculate  Factorial")
            print("2. Solve Compound Interest")
            print("3. Trigonometric Calculations")
            print("4. Area of Geometric Shapes")
            print("5. Back to Main Menu")

            choice = int(input("Enter your choice number (1-5)"))

            if choice == 1:
                 num = int(input("Enter the factorial number"))
                 fact = math.factorial(num)
                 print(f"factorial of {num} is: {fact}")

            elif choice == 2:
                money = int(input("Enter the money"))
                rate = int(input("Enter the rate of interest"))
                year = int(input("Enter the duration (in year)"))

                CI = money * (1 + rate/100) ** year
                print(f"Compound Interest is {CI}")

            elif choice == 3:
                value = int(input("Enter the Value"))
                radian = math.radians(value)
                print(f"sine is{math.sin(radian)}")
                print(f"cosine is{math.cos(radian)}")
                
            elif choice == 4:
                 print("Select an Option")
                 print("1.area of Square")
                 print("2. area of cylinder")

                 choice = float(input("Enter the choice number (1-2)"))

                 if choice == 1:
                        num = float(input("Enter the square number: "))
                        square = num * num
                        print("square number is:", square)

                 elif choice == 2:
                         r = float(input("Enter radius: "))
                         h = float(input("Enter height: "))
                         num = 2 * 3.14 * r * (r + h)
                         print("total area of cylinder =", num)
                 else:
                          print("Invalid Choice Number")

            elif choice == 5:
                 break
            else:
                print("Invalid Choice Number")
def random_operator(): 
      
      while True:
        print("Random Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List") 
        print("3. Create Random Password")
        print("4. Generate Random OTP") 
        print("5. Back to Main Menu")

        choice = int(input("Enter the Choice Number (1-5)"))

        if choice == 1:
            pass  
                 



def unique_uuid():

    id = uuid4()
    print(f"Generate Unique Identifiers (UUID) {id}")    

