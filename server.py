from flask import Flask, jsonify, request
from model import calc, scrape
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class Calc():
    BLAH = "test"

class Scraped():
    BLAHH = "test"

# immediately when you get to this domain
@app.route('/webscrape')
def getScrape():
    url_to_scrape = request.args.get('url')
    print(url_to_scrape)
    
    data = scrape.start_scrape(url_to_scrape)

    return jsonify({
        "cloth_type": data[0],
        "brand": data[1],
        "materials": data[2],
        "weight": data[3]
    })

@app.route('/')
def getCalc():
    
    return "Calc"


def main():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port = 80)