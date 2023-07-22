import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from filemgmt import read_from_csv
from selenium.webdriver.common.by import By
from DermaStore import Dermstore
import json

# open brands csv file
skincare_brands = read_from_csv('/Users/theodoreleeiv/AcneProducts/Data/skincare_brands.csv')

# For each brand collect data on each product type only select from moisturizers,cleansers,toners,
# serums,masks and do so by skin type and skin concern, key ingredients, preferences, prices and reviews
### open each brand url link
products = Dermstore()



skincare_products = []
### iterate through the brand instances
for skincare_brand in skincare_brands:
    brand = skincare_brand[0]
    brand_link = skincare_brand[1]
    products.url = brand_link
    ### use selenium to open the brand url links
    products.se_open_webpage_browser()

    ### filter the page by product type
    facet_value_to_find = ['Moisturisers','Cleansers','Toners','Serums','Exfoliators+%26+Scrubs']
    for facet_value in facet_value_to_find:
        try:
            css_selector = f'input[data-facet-value="{facet_value}"]'
            prod_type = products.se_get_element_selenium((By.CSS_SELECTOR,css_selector))
            products.move_to_element(prod_type)
            time.sleep(1)
            ### select a filter for product type
            prod_type.click()
            time.sleep(2)


            ### check for and close ad
            products.close_ad()

            #### return the html to be handled by beautiful soup
            html = products.driver.page_source
            soup = BeautifulSoup(html,'html.parser')
            product_items = soup.find_all('div', class_='productBlock')

            product_names = [item.find('h3', class_='productBlock_productName').text.strip() for item in product_items]
            product_links = [item.find('a', class_='productBlock_link')['href'] for item in product_items]

            for i in range(len(product_links)):
                product_data = {
                    'brand': brand,
                    'brand_link': brand_link,
                    'name': product_items[i].find('h3', class_='productBlock_productName').text.strip(),
                    'prod_link': product_items[i].find('a', class_='productBlock_link')['href'],
                    'type':facet_value,
                    'ingredients':None,
                    'reviews':None,
                    'number_of_reviews': None,
                    'ratings': None,
                    'price':None,
                    'product_description':None,
                    'size':None,
                    'skin_type':None,
                    'key_benefits': None
                }
                skincare_products.append(product_data)
                # Save each product_data as a JSON object to the file

            time.sleep(3)
            products.se_get_element_selenium((By.CSS_SELECTOR,css_selector)).click()
            time.sleep(1)
        except:
            print(facet_value,'Not in the list of filters')


#### store product names and url links in a json file
with open('Data/skincare_products.json', 'a') as json_file:
    json.dump(skincare_products, json_file, indent=2)
    json_file.write('\n,')  # Add a newline to separate objects


