from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
     def do_GET(self):
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_list = parse.parse_qsl(url_components.query)
        dictionary  = dict(query_list)


        if 'country' in dictionary :
            country = dictionary ['country']
            url = 'https://restcountries.com/v3.1/name/'
            response  = requests.get(url + country)
            data = response.json()
            capital = data[0]['capital'][0]
            message = f"The capital of {country} is {capital}"

        else:
            message = "Please provide me with a correct name"


        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return