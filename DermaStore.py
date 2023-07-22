from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
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
        self.prod_link = None #url for company
        self.brand_link = None  # url for company
        self.number_of_reviews = None
        self.ratings = None # ratings for the product
        self.price = None # price for the product
        self.product_description = None # how the product description
        self.size = None # size of the product, 0ml 10ml
        self.skin_type = None # what skin types is the product designed for
        self.key_benefits = None # what are the benefits of the product

""" Class to scrape the dermstore website"""
class Dermstore(AcneProduct):
    def __init__(self,url=None):
        self.url = url
        if self.url != None:
            r = requests.get(url)
            self.soup =  BeautifulSoup(r.content, 'html.parser')
        self.driver_path = '/Users/theodoreleeiv/Documents/Documents - Theodore’s MacBook Pro/chromedriver'
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        AcneProduct.__init__(self)


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
    #scroll an element into view

    def se_scroll_into_view(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def move_to_element(self,element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    # checks for and closes promotional ads
    def close_ad(self,max_attempts=3):
        attempt = 0
        while attempt < max_attempts:
            try:
                overlay = self.driver.find_element(By.ID, "attentive_overlay")
                if overlay:
                    # Use execute_script to set the "display" style property to "none"
                    self.driver.execute_script("arguments[0].style.display = 'none';", overlay)
                    print("Display set to none.")
                    return
            except NoSuchElementException:
                continue
            except StaleElementReferenceException:
                attempt += 1

        print("Failed to set display to none after multiple attempts.")
        try:
            # Wait for the "closeIconContainer" button to be clickable and click it
            self.close_ad()
        except Exception as e:
            print("Error while clicking the element:", str(e))











