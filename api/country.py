from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    # url_path = self.path
    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    dictionary = dict(query_string_list)

    if "name" in dictionary:
      url = "https://restcountries.com/v3.1/capital/"  
      country = dictionary["name"]
      response = requests.get(url + dictionary["name"])
      data = response.json()
      country = data[0]["name"]
      capital = str(country["name"])
      results = f"The capital of {country} is {capital}"

      self.send_response(200)
      self.send_header("Content-type","text/plain")
      self.end_headers()

      self.wfile.write(results.encode())
    else:
            message = "Please enter another capital"

    self.send_response(200)
    self.send_header("Content-type", "text/plain")
    self.end_headers()
    self.wfile.write(message.encode())
    return