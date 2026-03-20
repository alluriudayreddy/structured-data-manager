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
