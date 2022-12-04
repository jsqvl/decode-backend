from flask import Flask, jsonify, request

from model import calc, scrape

import requests
from flask_cors import CORS

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)
CORS(app)

class Calc():
    BLAH = "test"

class Scraped():
    BLAHH = "test"

# immediately when you get to this domain
@app.route('/webscrape')
def getScrape():
    # 
    url_to_scrape = request.args.get('url')
    blah_to_scrape = request.args.get('blah')
    print(blah_to_scrape)
    print(url_to_scrape)

    return "test"

@app.route('/')
def getCalc():
    
    return "Calc"


def main():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port = 80)