import requests
import enum

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClothType(Enum):
    JACKET = "jacket"
    PANTS = "pants"
    HAT = "hat"
    SHOES = "shoes"


def find_cloth_type(soup):

    return ""
    
def find_brand(soup):
    return ""

def find_materials(soup):
    return ""

def find_weight(soup):
    return 1

def start_scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, features = "html.parser")
    
    data = [find_cloth_type(soup), find_brand(soup), find_materials(soup), find_weight(soup)]

    return data