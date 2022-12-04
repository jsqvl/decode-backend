import traceback
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
    try:
        url_to_scrape = request.args.get('url')
        print(url_to_scrape)
        data = scrape.start_scrape(url_to_scrape)
    except:
        traceback.print_exc()
        print("Error processing, are you sure this is a valid url?")
        return "Error processing, are you sure this is a valid url?"

    return jsonify({
        "cloth_type": data[0],
        "brand": data[1],
        "materials": data[2],
        "num_washes": data[3],
        "weight_grams": data[4]
    })

@app.route('/submit')
def getCalc():
    try:
        calc_brand = request.args.get('brand')
        calc_cloth_type = request.args.get('cloth_type')
        calc_materials = request.args.get('materials')
        calc_num_washes = request.args.get('num_washes')
        calc_weight = request.args.get('weight')
        calc_data = calc.start_calc(calc_brand, calc_cloth_type, calc_materials, calc_weight)
    except:
        print("Error processing, check data submitted")
        return "Error processing, check data submitted"

    return jsonify({
        "sustainability_rating": calc_data[0],
        "fabric_quality": calc_data[1],
        "num_washes": calc_data[2],
        "num_washes": calc_data[3],
    })


def main():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port = 80)