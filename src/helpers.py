def generate_id(records):
    return len(records) + 1


def print_record(record):
    print("ID:", record["id"])
    print("Name:", record["name"])
    print("Category:", record["category"])
    print("Price:", record["price"])
    print("Quantity:", record["quantity"])
    print("Status:", record["status"])
    print("----------------------")