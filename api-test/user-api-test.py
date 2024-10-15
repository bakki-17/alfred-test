import pytest
import requests
from api_util.api_client import APIs
import json


@pytest.fixture(scope='module')
def api_client():
    return APIs()


def test_product_id_valid_response(api_client):
    response = api_client.get('/products/01J9ZP372WMJ4SN8YAKS1TK0EX')
    assert response.status_code == 200

    jsonData = response.json()
    
    #data to verify
    productName = "Plier"

    #Verify the json data 
    assert "name" in jsonData
    assert "category" in jsonData
    assert jsonData["category"]["name"] == productName

def test_product_id_invalid_response(api_client):
    response = api_client.get('/product/01J9ZP372WMJ4SN8YAKS1TK0EX')
    assert response.status_code == 200 #response code returns 404