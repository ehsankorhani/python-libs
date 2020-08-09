# REQUESTS - a Python HTTP library

```requests``` abstract the complexity of making http requests behind a simple API.

## Getting Started

Install the library with this pip command:

```bash
$ pip install requests
```

After installation it can be imported with:

```py
import requests
```

## Make HTTP Requests

### GET

This command will simply makes a GET requests to the provided URL:

```py
response = requests.get('https://reqres.in/api/users')
```

Any request has a response. even when it's unsuccessful. The ```response``` object will give you the ability to examine the result of the action.

```py
print (response.status_code) # <Response [200]> if success
```

The ```2xx``` responses are considered *success* and ```3xx``` indicate redirection and further actions. ```response``` object is truthy if it's status code is within this range. <br>
For instance, if the the endpoint returns 200:

```py
print (response == True) # False
```
But because the ```__bool__()``` method has been overloaded then:

```py
if (response):
    print('Success!') # Success!
```

```raise_for_status()``` also raises an exception if the response is not within the success range.

```py
from requests.exceptions import HTTPError

# ...

try:
    responseInvalid = requests.get('https://reqres.in/api/usersInvalid')
    responseInvalid.raise_for_status()
except HTTPError as http_err:
        print (f'An HTTP error occurred: {http_err}')
except Exception as err:
        print (f'An unknown error occurred: {err}')
else:
    print('Success!')
```

The code above will output an HTTPError:

```
An HTTP error occurred: 404 Client Error: Not Found for url: https://gorest.co.in/public-api/usersInvalid
```

### Response Content

In most cases we want to read the content that has been fetched with GET request. ```content``` property returns *raw bytes* of the response body.

```py
content = response.content
# b'{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg"},...}'
```

But if you provide the correct encoding, you can get an string representation of the body:
```py
response.encoding = 'utf-8' # default
responseText = response.text
# {"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg"},...
```

If you need the response to be serialized to JSON you can use:

```py
json = response.json()
```

### Response Headers

Occasionally it's required to read and take action on different ```HTTP headers```. The response object ```headers``` returns an key-value pairs of the different response headers.

```py
headers = response.headers
# {'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', ...
server = response.headers['Server']
# cloudflare
```

### Request Headers

In real integrations, almost always, you need to pass some type of headers along with the request. Here you can do it in this format:

```py
response = requests.get('https://reqres.in/api/users', headers = { 'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json' })
```

### Request Query String Parameters

To pass query strings along with the request, add them too the ```params```. This parameter accepts Dictionary/JSON value:

```py
response = requests.get('https://reqres.in/api/users', params = { 'name': 'John' })
```

Instead of *Dictionary*, you can pass *List of Tuples* or *Bytes*. However, in my opinion JSON is more descriptive.

### Other HTTP methods

```requests``` allows you to send all the other REST supported HTTP requests the same way as GET request.

```py
requests.post('https://reqres.in/api/users', data = { "name": "morpheus", "job": "leader" })
requests.put('https://reqres.in/api/users/2', data = { "name": "morpheus", "job": "zion resident" })
requests.delete('https://reqres.in/api/users/2')
requests.patch('https://reqres.in/api/users/2', data = { "job": "developer" })
requests.options('https://reqres.in/api/users') # supported verbs
requests.head('https://reqres.in/api/users') # information on user listing
```

### Request Body 

When you send a POST, PUT or PATCH request, you want to transfer data along as well.

If the ```Content-Type``` is ```application/x-www-form-urlencoded```, you can use ```data``` property to send the body:

```py
# dictionary
requests.post('https://reqres.in/api/users', data = { "name": "morpheus", "job": "leader" })
# list of tuples
requests.post('https://reqres.in/api/users', data = [("name", "morpheus"), ("job", "leader")])
```

And for the ```Content-Type = application/json``` you use the ```json``` property:

```py
requests.post('https://reqres.in/api/users', json = { "name": "morpheus", "job": "leader" })
```

<br>

## Authorization and Authentication

There are different implementations of server authentication.<br>
```requests.auth``` module provides objects for the different auth scenarios.

### Basic auth

It's the ```base64-encoded``` value of the *username* and *password*.

```py
import requests
from requests.auth import HTTPBasicAuth
# ...
response = requests.get('https://reqres.in/api/users', auth = HTTPBasicAuth('user', 'pass'))
```

Because basic auth is a common practice, Requests has provided a shorthand for it:

```py
response = requests.get('https://reqres.in/api/users', auth = ('user', 'pass'))
```

The ```AuthBase``` object of ```request.auth``` is extendable and you can use it to write your own customized authentication.

```py
from requests.auth import AuthBase

class CustomAuth(AuthBase):
    def __init__(self, token):
        self.token = token
    #...
```

And then use it as:

```py
response = requests.get('https://reqres.in/api/users', auth = CustomAuth('user', 'pass'))
```

### OAUTH 2

Is discussed separately in the **OAUTH 2.0** section.

<br>

## SSL Certificate

### References

* [Python’s Requests Library (Guide)](https://realpython.com/python-requests/)