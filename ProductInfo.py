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

class ProductInfo(AcneProduct):
    def __init__(self):
        AcneProduct.__init__(self)
        self.driver_path = '/Users/theodoreleeiv/Documents/Documents - Theodore’s MacBook Pro/chromedriver'
        self.driver = webdriver.Chrome(executable_path=self.driver_path)

    def get_size(self,element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

