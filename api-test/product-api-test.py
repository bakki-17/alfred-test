import requests 
import json
import random
import string
import pytest



def test_get_request():
     #base_url
    base_url = 'http://localhost:8091'
    url = base_url + '/products?by_brand=01J9ZP371T6XZPX6TW1DCHTZ2J'

    #auth_token
    auth_token = ''

    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200

    json_data = response.json()
    json_str = json.dumps( json_data, indent=4)
    print("json response body : ", json_str)
