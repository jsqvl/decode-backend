import requests
import re
import random

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Returns clothing type based on synonymous words dictionary
def find_cloth_type(soup):
    search_for_me = soup.find("h1").text.strip()
    print(search_for_me)

    clothes_enum_file = "./model/dictionaries/clothes.txt"
    with open(clothes_enum_file, "r+") as f:
        lines = f.readlines() # contains all the lines
        f.seek(0)
        count = 0
        for l in lines:
            strTest = " " + l.strip()
            if strTest.casefold() in search_for_me.casefold():
                if (count < 18 and count > 0):
                    return "hat"
                elif(count < 26 and count > 17):
                    return "jacket"
                elif(count < 34 and count > 25):
                    return "pants"
                elif(count < 44 and count > 33):
                    return "shirt"
                elif(count < 58 and count > 43):
                    return "shoes"
                elif(count > 57):
                    return "sweatshirt"
            count += 1
    return ""
    

# Returns brand by scraping through all SEC approved companies or website title if can't be found
def find_brand(soup):
    search_for_me = soup.find("h1").text.strip()
    print(search_for_me)
    brands_enum_file = "./model/dictionaries/brands.txt"
    with open(brands_enum_file, "r+") as f:
        lines = f.readlines() # contains all the lines
        f.seek(0)
        for l in lines:
            brand = l.strip()
            if brand in search_for_me:
                return brand
    return ""

# Final version will use regex to find the exact Cotton ratings
def find_materials(soup):
    # search_for_materials = soup.find_all(['p', 'span', 'li'])
    # print(search_for_materials)

    # # search through all tags for % signs
    # for tag in search_for_materials:
    #     # could be multiple %'s within a single p tag
    #     plain_text_tag = tag.text.strip()

    #     x = re.compile(r"^[1-9][0-9]?$|^100$%", re.IGNORECASE)
    #     x.match(plain_text_tag)
    #     if x:
    #         p1 = plain_text_tag.split(",")
    #         for i in p1:
    #             materials.append(i.strip())

    # Pseudo Materials Numbers
    


    materials_list = ["Cotton: 80%", "Polyester: 20%"]
            
    return materials_list

# Returns number of washes on page or -1 if can't find it
def find_num_washes(brand, materials):
    
    return -1

# Returns weight (to quantify material % make-up and improve energy calculations) or -1 if not present
def find_weight(soup):
    return 1

def start_scrape(url):
    ua = UserAgent()
    userAgent = ua.random
    userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    # print(userAgent)
    headers = {
        'User-Agent': str(userAgent),
        "referrer": "https://google.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": 'keep-alive',
    }

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, features = "html.parser")
    # print(soup)
    
    materials = find_materials(soup)
    brand = find_brand(soup)
    num_washes = find_num_washes(brand, materials)

    data = [
        find_cloth_type(soup), 
        brand, 
        materials, 
        num_washes, 
        find_weight(soup)]

    return data