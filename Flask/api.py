import flask
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True


products = [{
    "id": 0,
    "name": "Samsung Galaxy Note 2",
    "description": "Samsung tablet computer",
    "price": {
      "value": 299.99,
      "currency": "GBP"
    },
    "type": "Electrical",
    "department": "Computing",
    "weight": "569g"
  },
  {
    "id": 1,
    "name": "Breville Food Mixer 800W",
    "description": "Breville food mixer with bowl and multiple mixing arms. 800W max power",
    "price": {
      "value": 69.99,
      "currency": "GBP"
    },
    "type": "Electrical",
    "department": "Cookware",
    "weight": "2370g"
  },
  {
    "id": 2,
    "name": "Bosch Cordless Drill",
    "description": "Cordless drill with 12W charging unit",
    "price": {
      "value": 159.99,
      "currency": "GBP"
    },
    "type": "Electrical",
    "department": "DIY",
    "weight": "1579g"
  },
  {
    "id": 3,
    "name": "Amazon Voucher",
    "description": "Fifty Pounds Amazon Voucher Card",
    "price": {
      "value": 50,
      "currency": "GBP"
    },
    "type": "Voucher",
    "department": "Gifts",
    "weight": "5g"
  },
  {
    "id": 4,
    "name": "Kitchen Scales",
    "description": "Traditional Kitchen Scales",
    "price": {
      "value": 79.99,
      "currency": "GBP"
    },
    "type": "Electrical",
    "department": "Cookwares",
    "weight": "1057g"
  },
  {
    "id": 5,
    "name": "Pass the Driving Test",
    "description": "Book - Pass your driving test - Penguin publishers",
    "price": {
      "value": 7.99,
      "currency": "GBP"
    },
    "type": "Book",
    "department": "Books and Stationery",
    "weight": "57g"
  },
  {
    "id": 6,
    "name": "Raspberry Pi Zero",
    "description": "Raspberry PI Zero Computer",
    "price": {
      "value": 4.8,
      "currency": "GBP"
    },
    "type": "Electrical",
    "department": "Computing",
    "weight": "30g"
  },
  {
    "id": 7,
    "name": "Clean Code",
    "description": "Clean Code: A Handbook of Agile Software Craftsmanship (Robert C. Martin)",
    "price": {
      "value": 18.99,
      "currency": "GBP"
    },
    "type": "Book",
    "department": "Books and Stationery",
    "weight": "220g"
  },
  {
    "id": 8,
    "name": "Asics Gel-Nimbus 19",
    "description": "Asics Gel-Nimbus 19 Running shoes",
    "price": {
      "value": 108.5,
      "currency": "GBP"
    },
    "type": "Running",
    "department": "Shoes",
    "weight": "150g"
  },
  {
    "id": 9,
    "name": "Mr Happy Mug",
    "description": "Mr Men Mug. Mr Happy. 300ml",
    "price": {
      "value": 8.5,
      "currency": "GBP"
    },
    "type": "Ceramics",
    "department": "Home",
    "weight": "110g"
  },
  {
    "id": 10,
    "name": "Asics Gel-Nimbus 19",
    "description": "Asics Gel-Nimbus 19 Running shoes",
    "price": {
      "value": 108.5,
      "currency": "GBP"
    },
    "type": "Running",
    "department": "Shoes",
    "weight": "150g"
  },
  {
    "id": 11,
    "name": "Canon EF 75-300mm f/4.0-5.6 III Lens",
    "description": "Canon EF 75-300mm f/4.0-5.6 III Lens",
    "price": {
      "value": 124.76,
      "currency": "GBP"
    },
    "type": "Electrical",
    "department": "Photography and Art",
    "weight": "460g"
  },
  {
    "id": 12,
    "name": "YongNuo YN-560 III Flashgun",
    "description": "YongNuo YN-560 III Flashgun",
    "price": {
      "value": 47.95,
      "currency": "GBP"
    },
    "type": "Electronics",
    "department": "Photography and Art",
    "weight": "260g"
  },
  {
    "id": 13,
    "name": "Amazon Echo",
    "description": "Amazon Echo, White",
    "price": {
      "value": 149.99,
      "currency": "GBP"
    },
    "type": "Electrical",
    "department": "Entertainment",
    "weight": "1098g"
  },
  {
    "id": 14,
    "name": "Sketcher Twinkle Toes",
    "description": "Pink Sketcher Twinkle Toe sandals with light up sole",
    "price": {
      "value": 19.99,
      "currency": "GBP"
    },
    "type": "Casual",
    "department": "Shoes",
    "weight": "100g"
  },
]

# Base URL
@app.route('/', methods=['GET'])
def home():
    return "<h1>Jake is winning!</h1>"

# API route for all products
@app.route('/api/v1/resources/products/all', methods=['GET'])
def api_all():
    return jsonify(products)

# API route for querying products
@app.route('/api/v1/resources/products', methods=['GEt'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: no id field provided. Have a word with yourself"

    results = []

    for product in products:
        if product['id'] == id:
            results.append(product)

    return jsonify(results)


app.run()

