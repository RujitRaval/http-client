#!/usr/bin/python3
"""
Author: Rujit Raval
email: rujitraval@gmail.com
"""

import json
import requests

HEADERS = ""

def login():
    """
    Parameters:
    None

    Returns:
    string: Returns the header to be appended on GET request.
    """
    try:
        # Setting API endpoint for login
        login_api_endpoint = "http://localhost:5000/api/login"

        # Setting authentication payload
        auth_payload = {"username": "gest", "password": "guest"}

        # HTTP POST request to the Login API with authentication payload
        response = requests.post(url=login_api_endpoint, data=json.dumps(auth_payload).encode())

        if not response.status_code == 401:
            print("Invalid credentials.")
            exit()
        if not response.text.startswith('{"access_token": '):
            print("Invalid access token from HTTP Server.")
            exit()
        token = response.text
        token_data = json.loads(token)
        my_token = token_data["access_token"]

        # Setting up the header to append in GET request
        headers = {'Authorization' : 'Bearer %s' %  my_token}
        return headers

    # HTTP Server or Login API cannot be reached
    except requests.exceptions.ConnectionError:
        print("HTTP server is not reachable.")
        exit()

def get_me(url, headers):
    """
    Parameters:
    url: string | API endpoint for HTTP request.
    headers: string | Header to append in HTTP get request.

    Returns:
    string | Response provided by HTTP GET request.
    """
    try:
        api_response = requests.get(url=url, headers=headers)
        if api_response.status_code != 200:
            headers = login()
            return get_me(url, headers)
        return api_response.text

    except requests.exceptions.ConnectionError:
        return "{} API is not reachable.".format(url)

if __name__ == "__main__":
    URLS = ["http://localhost:5000/api/secret1",
            "http://localhost:5000/api/secret2",
            "http://localhost:5000/api/secret3"]
    HEADERS = login()
    for api in URLS:
        print(get_me(api, HEADERS))
