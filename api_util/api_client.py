import requests

class APIs: 
    BASE_URL = 'http://localhost:8091/'

    def __init__(self):
        self.header = {
            "Content-Type": "application/json",
            "accept": "application/json"
        }
    
    def get(self, endpoint):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.get(url, headers=self.header)
        return response
    
    def post(self, endpoint, data):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.post(url, headers=self.header, json=data)
        return response