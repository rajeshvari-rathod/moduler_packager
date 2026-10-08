from package.math_utils import dt_operator

def main():
    while True:
        print("================================")
        print("Welcome to Multi-Utility Toolkit")
        print("================================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File operations (Custom Module)")
        print("6. Explore Module Attributes(dir())")
        print("7. Exit")
        print("================================")

        choice = int(input("Enter your choice number(1-7):"))

        if choice == 1:
            dt_operator()

        elif choice == 2:
                   pass
       
        elif choice == 3:
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            pass

        elif choice == 7:
            print("Thank you for using Multi-Utility Toolkit . Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")   
    
        
if __name__ == "__main__":
    main()            
