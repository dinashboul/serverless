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
            url = "https://restcountries.com/v3.1/name/" 
            base_url = url + dictionary['name']
            response = requests.get(base_url)
            data = response.json()
            capital = data[0]['capital']
            message = str(capital[0])
            final = f'the capital of {query} is {message}'
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(final.encode())
        else:
            message = "Please enter another country"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

        return