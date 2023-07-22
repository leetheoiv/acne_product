from ProductInfo import ProductInfo
from bs4 import BeautifulSoup
import requests

def bs4_get_element(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


product_info = ProductInfo()

# for every product page write to a csv file
### write code to open the json file with links and pass them into bs4
soup = bs4_get_element()

### Extract the size from the title of the product]

### Get the number of reviews

### Get the reviews in a list

### Get the price (MSRP) and Retailer Price

### Get the product description

### Get all at a Glance information

### Get the Ingredients in list form