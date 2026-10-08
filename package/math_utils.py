from datetime import datetime
import time

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

            first1 = datetime.strptime("%Y/%m/%d",first1)
            second2 = datetime.strptime("%Y/%m/%d",second2)

            new_dt = abs(first1-second2)
            print(f"Difference between two date is: {new_dt}")

        elif choice == 3:
             current_dt = datetime.now()


        elif choice == 4:
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            pass
        