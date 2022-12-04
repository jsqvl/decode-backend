## Python Backend
Welcome to DECODE's back-end. A honey-like sustainable product calculator.

To test product URL web-scraping, paste:
localhost/webscrape?url={insert url of below here}

Shirt
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
    num_washes: 125
    weight_grams: 890
}

