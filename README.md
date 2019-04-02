# HTTP CLIENT

An HTTP client program that can execute requests against the API server.

To run the API client:

1. Ensure you have a valid version of Python 3.6+ installed

2. Clone this repository:
```
$ git clone https://github.com/secberus/homework-api
```

3. Run the server
```
$ cd homework-api
$ ./run.py
```

4. Run the client
```
$ cd homework-api
$ python api_client.py
```

## Requirements:

Please use Python3 (3.6+).

This HTTP client application can execute the following HTTP requests sequentially against the server.

1. `GET http://localhost:5000/api/secret1`
2. `GET http://localhost:5000/api/secret2`
3. `GET http://localhost:5000/api/secret3`

The first step is to login to the server by executing a `POST` request to the authentication endpoint at `http://localhost:5000/api/login`.

The authentication payload should is set as:
```
{
  "username": "guest",
  "password": "guest"
}
```

A successful login request results in a response from the server with the following format:
```
{
  "access_token": "89a35947-5360-4731-9b69-f8d683c4d778"
}
```

The value of the `access_token` is included as header in the `GET` requests above.

```
Authorization: Bearer <access_token_value>
```

The `access_token` is only good for a short period, after which time, client will have to authenticate again to continue querying the `GET` API URIs.  
Client program will gracefully handles the `401: Unauthorized` response status from the API and re-authenticate.

## Error Handling:

* **HTTP Server not reachable:**
HTTP client is capable of handling the situation where HTTP server is not running or not reachable when sending login credentials and getting the token. It handles the exception *requests.exceptions.ConnectionError* and displays the message as:
```
HTTP server is not reachable.
```

* **Invalid Login credentials:**
HTTP client handles the situation when HTTP client sends login credential successfully to the HTTP server but  either username or password is invalid.
When HTTP server returns the status code as *401 : Unauthorized*, it displays the message as:
```
Invalid credentials.
```

* **Invalid token response from HTTP server:**
Upon successful login request HTTP client expects access_token from HTTP server in following format:
```
{
  "access_token": "89a35947-5360-4731-9b69-f8d683c4d778"
}
```
If the response from server is not in the same format it displays the message as:
```
Invalid access token from HTTP Server.
```

* **Handling API unreachable:**
HTTP client is capable to handle the situation where one of the requested API is not reachable. The HTTP client displays the notification for specific API and continues with the next HTTP GET request.
It shows the message as:
```
http://localost:5000/api/secretN API is not reachable. (N can be 1/2/3.)
```
