records = []
current_id = 1

def main():

    while True:

        print("/nStructured data manager")
        print("1. Add Record")
        print("2. Exit Program")

        choice = input("Enter your Choice: ")
        if choice == "1":
            pass #add_record() will be added later
        elif choice == "2":
            print("Exiting program.....")
            break
        else:
            print("Invaid choice. Please try again.")


if __name__ == "__main__":
    main()