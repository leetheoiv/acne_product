from Dermstore import Dermstore
from selenium.webdriver.common.by import By
import json
import time
import re

# Opening JSON file
with open('/Users/theodoreleeiv/AcneProducts/Data/skincare_products.json','r') as json_file:
    data = json.load(json_file)
    ## collect and update product data in json file accordingly
    for product in data:
        ### Pass Links into Dermstore Instance
        product_page_link = f"https://www.dermstore.com{product['prod_link']}"
        skincare_product = Dermstore(product_page_link)
        skincare_product.se_open_webpage_browser()

        ### click all dropdowns
        infobox = skincare_product.se_get_element(By.CLASS_NAME,'athenaProductDescription_contentPropertyList')
        skincare_product.move_to_element(infobox)
        time.sleep(1)
        skincare_product.close_ad()
        infobox_elements = infobox.find_elements(By.CSS_SELECTOR,'div[data-item]')

        data_item = {}
        for infobox_element in infobox_elements:
            try:
                data_category = infobox_element.find_element(By.CLASS_NAME,'productDescription_accordionControl').text
                infobox_element.click()
                data_item[data_category] = infobox_element.text
            except:
                continue
        print(data_item)

        ### return page html
        html = skincare_product.get_product_html()

        ### Read the html into bs4
        soup = skincare_product.bs4_get_soup(html)


        ### Get the number of reviews
        num_reviews = soup.find('p',{'class':'athenaProductReviews_reviewCount Auto'})
        num_reviews = num_reviews.text if num_reviews else 0
        product['number_of_reviews'] = num_reviews

        ### Get all reviews link
        reviews_link = soup.find('a',{'class':'athenaProductReviews_seeReviewsButton'})
        reviews_link = reviews_link['href'] if reviews_link else None
        product['reviews'] = reviews_link

        ### Get rating
        rating = soup.find('span', {'class': 'athenaProductReviews_aggregateRatingValue'})
        rating = rating.text.strip() if rating else 0
        product['score'] = rating

        ### Get Number of ratings
        number_of_ratings = soup.find_all('span', {'class': 'athenaProductReviews_ratingBreakdown_hiddenLabel'})
        if len(number_of_ratings) != 0 or None:
            rating_types = [rating.text for rating in number_of_ratings]
            product['ratings'] = rating_types

        ### Get the price (MSRP) and Retailer Price
        MSRP = soup.find('p',{'class':'productPrice_rrp'})
        derm_price = soup.find('p',{'data-product-price':'price'})
        derm_price = derm_price.text.strip() if derm_price else None
        MSRP = MSRP.text.strip() if MSRP else None

        if MSRP == None:
            MSRP = derm_price
        product['MSRP'] = MSRP
        product['price'] = derm_price

        ### Get the product description
        product['product_description'] = data_item['Product Overview']
        ### Get all at a Glance information
        product['overview'] = data_item['At a Glance']

        ### Get the Ingredients in list form
        product['ingredients'] = data_item['Ingredients']

        ### Update the JSON file with the modified product info
        with open('/Users/theodoreleeiv/AcneProducts/Data/skincare_products.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)

