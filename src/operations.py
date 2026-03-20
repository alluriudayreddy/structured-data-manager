def add_record(records):
    name = input("Enteer name: ")
    category = input("Enter category: ")
    price = input("Enter prince: ")
    quantity = input("Enter quantity: ")
    status = input("Enter status: ")

    current_id = len(records) + 1

    record = {
        "id": current_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "status": status,
    }
    
    records.append(record)
    print("Record added successfully!")


def view_records(records):
    if len(records) == 0:
        print("No record found.")
        return
    
    for record in records:
        print(record)


def search_record(records):
    field = input("search by id/name/category/price/quantity/status: ")

    if len(records) > 0 and field not in records[0]:
        print("Invalid field. Please try again.")
        return
    
    value = input("Enter the Value you want to search for: ")

    found = False

    for record in records:
        if str(record[field]) == value:
            print(record)
            found = True
    
    if not found:
        print("No record found with the given value.")
        
