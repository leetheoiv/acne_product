from DermaStore import Dermstore,AcneProduct
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Get the dermatology brands and their page urls and create a list of acne product instances
derm_brands = Dermstore('https://www.dermstore.com/brands.list')
brands = derm_brands.bs4_get_element(derm_brands.soup.find_all('li',class_='responsiveBrandsPageScroll_brandTabsItem'))
skincare_products = []
for i in range(len(brands)):
    acneprod = AcneProduct()
    acneprod.brand = brands[i].text.strip()
    acneprod.link = brands[i].find('a')['href']
    skincare_products.append(acneprod)

# For each brand collect data on each product type only select from moisturizers,cleansers,toners,
# serums,masks and do so by skin type and skin concern, key ingredients, preferences, prices and reviews
### iterate through the brand instances
for skincare_product in skincare_products:
    ### open each brand url link
    brand_page = Dermstore(skincare_product.link)
    ### use selenium to open the brand url links
    brand_page.se_open_webpage_browser()
    ### filter the page by product type
    facet_value_to_find = ['Moisturisers','Cleansers','Toners','Serums','Exfoliators+%26+Scrubs']
    for facet_value in facet_value_to_find:
        css_selector = f'input[data-facet-value="{facet_value}"]'
        prod_type = brand_page.se_get_element_selenium((By.CSS_SELECTOR,css_selector))
        ### select a filter for product type
        prod_type.click()
        time.sleep(1)

        ### check for and close ad
        brand_page.close_ad(By.ID, value="closeIconContainer")

        #### return the html to be handled by beautiful soup
        html = brand_page.driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        print(soup)
        product = soup.find_all('div',class_='productBlock_itemDetails_wrapper ')
        print(product)
        prod_type.click()

        #### store product names and url links in a json file



