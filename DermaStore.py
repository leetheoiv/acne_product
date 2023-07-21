from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup


"""Creates a class for the acne products"""
class AcneProduct:
    def __init__(self):
        self.brand = None # contains the brand name
        self.name = None # the products actual name
        self.type = None # what type of product it is
        self.ingredients = None # will be a list of ingredients
        self.reviews = None # will be a list of reviews
        self.link = None #url for company
        self.number_of_reviews = None
        self.ratings = None # ratings for the product
        self.price = None # price for the product
        self.product_description = None # how the product description
        self.size = None # size of the product, 0ml 10ml
        self.skin_type = None # what skin types is the product designed for
        self.key_benefits = None # what are the benefits of the product

""" Class to scrape the dermstore website"""
class Dermstore(AcneProduct):
    def __init__(self,url):
        self.url = url
        r = requests.get(url)
        self.soup =  BeautifulSoup(r.content, 'html.parser')
        AcneProduct.__init__(self)
        self.driver_path = '/Users/theodoreleeiv/Documents/Documents - Theodore’s MacBook Pro/chromedriver'
        self.driver = webdriver.Chrome(executable_path=self.driver_path)

    # searches and returns the desired element using bs4
    def bs4_get_element(self,soup_func,new_soup=None,new_bs4=False):
        if new_bs4 == True:
            soup = new_soup
            element = soup_func
            return element
        else:
            element = soup_func
            return element

    # opens a webpage using selenium
    def se_open_webpage_browser(self):
        self.driver.get(self.url)
        time.sleep(1)

    # searches and returns the desired element using selenium
    def se_get_element_selenium(self,func):
        # Wait for the element to be present
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(func))
        return element

    # checks for and closes promotional ads
    def close_ad(self,by, value, max_attempts=3):
        attempt = 0
        while attempt < max_attempts:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((by, value))
                )
                element.click()
                print("Clicked the element successfully.")
                return
            except StaleElementReferenceException:
                attempt += 1
        print("Failed to click the element after multiple attempts.")

        try:
            # Wait for the "closeIconContainer" button to be clickable and click it
            self.close_ad(by=By.ID, value="closeIconContainer")
        except Exception as e:
            print("Error while clicking the element:", str(e))











