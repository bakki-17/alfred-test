import requests 
import json
import random
import string
import pytest

#base_url
base_url = 'http://localhost:8091'

#auth_token
auth_token = ''

def test_get_product_by_brand():
    
    url = base_url + '/products?by_brand=01J9ZP371T6XZPX6TW1DCHTZ2J'

    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200

    json_data = response.json()
    json_str = json.dumps( json_data, indent=4)
    print("json response body : ", json_str)

def test_get_product_byID():
    
    url = base_url + '/products/01J9ZP372WMJ4SN8YAKS1TK0EX'

    headers = {'Authorization': auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    # assert response.headers["Content-Type"] == "application/json; charset=UTF-8"


    price = 14.15
    is_location_offer = False
    is_rental = False
    product_name = 'Pliers'
    brand_name = "ForgeFlex Tools"

    category_array = { 'id': '01J9ZP372CW17V40KPJ3VFGDTT',
        'name': 'Pliers',
       'parent_id': '01J9ZP3727168BEJKSCRC33E4T',
       'slug': 'pliers'}
    

    json_data = response.json()
   
    # print the json response
    json_str = json.dumps(json_data, indent=2)
    print('\n\njson response for Product Id : ', json_str)


    assert "product_image" in json_data
    assert "is_rental" in json_data

    assert json_data["category"] == category_array
    assert json_data["category"]["name"] == product_name
    assert json_data["brand"]["name"] == brand_name

    assert type(json_data["name"]) == str
    assert type(json_data["id"]) == str
    assert type(json_data["is_rental"]) == bool


    # assert json_data['price'] == price
    # for products in json_data:
        # assert products['name'] == prod_name
    #     assert products["is_location_offer"]
    #     assert products["is_rental"]
    