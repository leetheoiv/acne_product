import json
import csv
def store_skincare_products_to_json(skincare_products, filename):
    # Convert the list of skincare products to a list of dictionaries
    products_list = []
    for product in skincare_products:
        product_dict = {
            'brand': product.brand,
            'link': product.link
        }
        products_list.append(product_dict)
        # Write the list of dictionaries to a JSON file
        with open(filename, 'w') as json_file:
            json.dump(products_list, json_file)

def save_to_csv(filename,action,data=None,fieldnames=None):
    # Create or open the CSV file in write mode
    with open(filename, action, newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write the header row to the CSV file
        writer.writerow(fieldnames)
        # Write each product as a row in the CSV file
        writer.writerow(data)

def read_from_csv(filename):
    rows = []
    # Create or open the CSV file in write mode
    with open(filename, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        # Skip the header row
        next(reader)
        # Read each row and create AcneProduct objects
        for row in reader:
            rows.append(row)
    return rows

