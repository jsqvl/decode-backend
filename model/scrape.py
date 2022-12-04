import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Soup (which contains the html) -> search the html for h1 -> 
def find_cloth_type(soup):
    search_for_me = soup.find("h1").text.strip()
    print(search_for_me)

    clothes_enum_file = "./model/dictionaries/clothes.txt"
    with open(clothes_enum_file, "r+") as f:
        lines = f.readlines() # contains all the lines
        f.seek(0)
        count = 0
        for l in lines:
            if l.strip() in search_for_me:
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

def find_materials(soup):
    search_for_materials = soup.find_all('p', 'span', 'li')
    #print(search_for_p)
    #search_for_span = soup.find_all('span', string="%")
    #print(search_for_span)
    #search_for_li = soup.find_all('li', string="%")
    #print(search_for_li)
    
    materials = []

    if search_for_materials is not False:
        # could be multiple p tags with %'s in them
        for p in search_for_materials:
            # could be multiple %'s within a single p tag
            p1 = p.split(",")
            for i in p1:
                materials.append(i)

    # if search_for_span is not False:
    #     for s in search_for_span:
    #         s2 = s.split(",")
    #         for i in s2:
    #             materials.append(i)

    # if search_for_li is not False:
    #     for l in search_for_li:
    #         l3 = l.split(",")
    #         for i in li:
    #             materials.append(i)
            
    return materials

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
    
    data = [find_cloth_type(soup), find_brand(soup), find_materials(soup), find_weight(soup)]

    return data