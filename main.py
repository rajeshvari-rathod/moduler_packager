from package.math_utils import dt_operator,math_operator,unique_uuid,random_operator
from package.explore_module import explore_module
from package.file_utils import file_operator
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
            math_operator()
       
        elif choice == 3:
            random_operator()

        elif choice == 4:
            unique_uuid()

        elif choice == 5:
             file_operator()

        elif choice == 6:
            explore_module()

        elif choice == 7:
            print("Thank you for using Multi-Utility Toolkit . Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")   
    
        
if __name__ == "__main__":
    main()            
