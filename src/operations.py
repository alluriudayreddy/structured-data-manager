import helpers

def add_record(records):

    name = input("Enter name: ")
    category = input("Enter category: ")
    price = input("Enter price: ")
    quantity = input("Enter quantity: ")
    status = input("Enter status: ")

    current_id = helpers.generate_id(records)

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
    helpers.print_record(record)
    return True


def view_records(records):
    if len(records) == 0:
        print("No record found.")
        return
    
    for record in records:
        helpers.print_record(record)


def search_record(records):
    field = input("search by id/name/category/price/quantity/status: ")

    if len(records) > 0 and field not in records[0]:
        print("Invalid field. Please try again.")
        return
    
    value = input("Enter the Value you want to search for: ")

    found = False

    for record in records:
        if str(record[field]) == value:
            helpers.print_record(record)
            found = True
    
    if not found:
        print("No record found with the given value.")


def update_record(records):
    record_id = input("Enter the ID of the record you want to update: ")
    found = False

    for record in records:
        if str(record["id"]) == record_id:

            field = input("Enter the field you want to update name/category/price/quantity/status: ")
             
            if field not in record:
                print("Invalid field. Pllease try again.")
                return
            
            new_value = input("Enter the new value: ")

            record[field] = new_value
            print("Record updated successfully!")
            helpers.print_record(record)
            found = True
            break

    if not found:
        print("No record found with the given ID.")


def delete_record(records):

    record_id = input("Enter the ID of the record you want to delete: ")
    found = False

    for record in records:
        if str(record["id"]) == record_id:
            records.remove(record)
            print("Record deleted successfully!")
            found = True
            break

    if not found:
        print("No record found with the given ID.")


def filter_records(records):

    field = input("Filter by name/category/price/quantity/status: ")

    if len(records) > 0 and field not in records[0]:
        print("Invalid field. Please try again.")
        return
    
    value = input("Enter the value you want to filter by: ")

    found = False
    
    for record in records:
        if str(record[field]) == value:
            helpers.print_record(record)
            found = True

    if not found:
        print("No record found with the given value.")


def sort_records(records):

    field = input("Sort by name/category/price/quantity/status: ")

    if len(records) > 0 and field not in records[0]:
        print("Invalid field. Please try again.")
        return
    
    order = input("Enter the sort order (asc/desc): ")

    def get_value(record):
        return record[field]
    
    if order == "desc":
        sorted_records = sorted(records, key=get_value, reverse=True)
    else:
        sorted_records = sorted(records, key=get_value)

    for record in sorted_records:
        helpers.print_record(record)