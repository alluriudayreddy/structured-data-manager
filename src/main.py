import operations

records = []

def main():
    
    while True:
        print("\nStructured Data Manager")
        print("1. Add Record")
        print("2. View Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Filter Records")
        print("7. Sort Records")
        print("8. Exit Program")

        choice = input("Enter your Choice: ")

        if choice == "1":
            operations.add_record(records)

        elif choice == "2":
            operations.view_records(records)

        elif choice == "3":
            operations.search_record(records)

        elif choice == "4":
            operations.update_record(records)

        elif choice == "5":
            operations.delete_record(records)

        elif choice == "6":
            operations.filter_records(records)

        elif choice == "7":
            operations.sort_records(records)

        elif choice == "8":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()