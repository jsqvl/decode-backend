import requests

from bs4 import BeautifulSoup

# Soup (which contains the html) -> search the html for h1 -> 
def find_cloth_type(soup):
    search_for_me = soup.find("h1")[0].text.strip()

    with open("./dictionaries/clothes", "r+") as f:
        lines = f.readlines() # contains all the lines
        f.seek(0)
        count = 0
        for l in lines:
            if l in search_for_me:
                if (count < 20 and count > 0):
                    return "hat"
                elif(count < 29 and count > 20):
                    return "jacket"
                elif(count < 38 and count > 29):
                    return "pants"
                elif(count < 49 and count > 38):
                    return "shirt"
                elif(count < 65 and count > 49):
                    return "shoes"
                elif(count > 65):
                    return "sweatshirt"
            count += 1
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