from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_list)

        if 'name' in dictionary:
            query = dictionary['name']
            url = 'https://restcountries.com/v3.1/name/'
            base_url = url + query
            response = requests.get(base_url)
            data = response.json()
            capital = data[0]['capital'][0]
            message = f"The capital of {query} is {capital}"

        elif 'name' in dictionary:
            url = 'https://restcountries.com/v3.1/capital/'  
            capital = dictionary["name"]
            response = requests.get(url + capital )
            data = response.json()
            country = data[0]['name']['common']
            # capital = str(country["name"])
            message = f"The {country} is capital of {capital}"

        else:
            message = "Please enter another country or another capital"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

        return