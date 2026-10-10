
def create_file():
    try:
        name = input("Enter a file name")
        with open (name,"x") as file:
            print("file create successfully")
    except:
        print("file exists")

def add_entry():
    try:
        name = input("Enter a new file")
        new_entery = input("Enter your data  to write")
        with open(name,"w") as file:
            file.write(new_entery)
            print("entery data to  write successfully")
    except:
            print("Invalid file data")

def read_file():
    try:
        file = input("Enter a file name")
        with open(file,"r") as file:
            data = file.read()
            print("file content")
            print(data)  
    except:
        print("this file dosen't exists")

def append_file():
    try:
         file = input("Enter a file name")
         data = input("Enter a data append")
         with open(file,"a") as file:
             file.write(data + "\n")
             print("data append successfully")
    except:
         print("Invalid data")    

def update_file():
    try:
        file = input("Enter a file name")
        oldfile = input("Enter the replace").strip()
        newfile = input("Enter a new file name").strip() 

        with open(file,"r") as file:
            data = file.read()

            if oldfile.strip() in data:
                data = data.replace(oldfile,newfile)

                with open(file,"w") as file:
                    file.write(data)

                print("Entery update")

            else:
                print("entery not found")

    except:
        print("Invalid file")                 
def file_operator():
    while True:
        print("File Operations") 
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Update to a file")
        print("6. Back to Main Menu")

        choice = int(input("Enter your choice Number (1-5)"))

        if choice == 1:
            create_file()

        elif choice == 2:
            add_entry()

        elif choice == 3:
            read_file()

        elif choice == 4:
            append_file()

        elif choice == 5:
              update_file()

        elif choice == 6:    
            break

        else:
            print("Invalid Choice Number")     
        