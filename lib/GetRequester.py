import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        pass
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        pass
        
        parsed_data = json.loads(self.get_response_body())
        return parsed_data