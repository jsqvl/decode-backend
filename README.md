# Decode Backend
Welcome to the backend powering DECODE, the chrome extension that which helps you make greener decisions on apparel products.

More details: https://devpost.com/software/decode-z8ecsg

Front-end Code: https://github.com/shawnesquivel/sustain-hacks


## How it works
    1. Signalled by opening the front-end, processes an HTTP request and fulfils it by web-scraping the current product page's data, converting it to a JSON, and returning it to the front-end for auto-fill

    2. Signalled by the extension submit button, the form information is passed via the local-host URL call, python requests separates the passed arguments, does the calculations, and returns it 

## How it was built


## Challenges
While the initial portion of our project went smooth, coding at an attainable and functional level of code given the time alotted seemed to be more challenging than expected.
By starting from scratch without any previous understanding of chrome-extensions and flask, we ran into lots of compatibility issues meshing the two.
## Accomplishments


## Lessons learned


## Where does it go from here?


## Instructions
1. See requirements.txt for the required modules/versions and install them

2. Open a terminal in the root directory

3. Run the command 'python server.py'

4. Now, on a browser, we can test the following.

a)
To test product URL web-scraping, paste:
localhost/webscrape?url={insert url of below here}

Example Shirt
https://www.urbanoutfitters.com/en-ca/shop/standard-cloth-angus-popover-polo-shirt?category=SEARCHRESULTS&color=011&searchparams=q%3Dshirt&type=REGULAR&quantity=1

Jacket
https://www.adidas.ca/en/polar-fleece-nature-allover-print-1-4-zip-jacket/HK4575.html

Jeans
https://ca.shein.com/High-Waist-Slant-Pocket-Straight-Leg-Jeans-p-2846834-cat-1934.html?src_identifier=st%3D2%60sc%3Djeans%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_search1670150132131&mallCode=1&scici=Search~~EditSearch~~1~~jeans~~~~0

Example Jsonified Web-scraped Data:
{
    brand: "SHEIN"
    cloth_type: "pants"
    materials: [
        "Cotton: 62%",
        "Polyester: 37%",
        "Viscose 1%"
    ]
    num_washes: 200
    weight_grams: 890
}

To test the product sustainability calculator, paste:
http://localhost:80/submit?brand=$Nike&cloth_type=$Jacket&materialone=$Polyester&materialtwo=$Cotton&num_washes=$125&weight=$800

localhost/submit$brand=Nike&cloth_type=jacket&
Example Jsonified Calculations:
{
    sustainability_rating: 100
    fabric_quality: 67
    num_washes: 125
}