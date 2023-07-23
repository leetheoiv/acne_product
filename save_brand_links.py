from Dermstore import Dermstore,AcneProduct
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

# Get the dermatology brands and their page urls and create a list of acne product instances
derm_brands = Dermstore('https://www.dermstore.com/brands.list')
brands = derm_brands.bs4_get_element(derm_brands.soup.find_all('li',class_='responsiveBrandsPageScroll_brandTabsItem'))
skincare_brands = []
for i in range(len(brands)):
    brand = brands[i].text.strip()
    brand_link = brands[i].find('a')['href']
    skincare_brands.append((brand,brand_link))

with open('Data/skincare_brands.csv', 'a', newline='') as csv_file:
    fieldnames = ['brand', 'link']
    writer = csv.writer(csv_file)
    # Write the header row to the CSV file
    writer.writerow(fieldnames)
    # Write each product as a row in the CSV file
    for brand in skincare_brands:
        brand_name = brand[0]
        brand_link = brand[1]
        writer.writerow([brand_name,brand_link])




