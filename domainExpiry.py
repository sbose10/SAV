"""
Program parses json from a url to provide the expiration date

Author : Sonita Bose
"""

import ssl
from urllib.request import Request, urlopen,socket
from urllib.error import URLError, HTTPError
from ast import literal_eval
import json
port = '443'    # secure web browser communication or HTTPS services
url = input('Enter only domain name ')  # Accepting the url from user

host_name = url
context = ssl.create_default_context()  # Access the Transport Security Layer

with socket.create_connection((host_name, port)) as sock:  # Creating a connection with the TCP layer with the hostname and port
    with context.wrap_socket(sock, server_hostname=host_name) as ssock:
        details = json.dumps(ssock.getpeercert())  # Parsing json
        details_converted = literal_eval(details)  # Converting dict from json

print('\nEntire json:', details)  # Printing entire json
print('\nNot before:', details_converted["notBefore"])  # Printing the not before date attribute to console
print('\nNot After:', details_converted["notAfter"])  # Printing the not after date attribute to console
