import requests
from requests.exceptions import HTTPError

response = requests.get('https://reqres.in/api/users')


print (response == True)

if (response):
    print('Success!')

try:
    responseInvalid = requests.get('https://reqres.in/api/usersInvalid')
    responseInvalid.raise_for_status()
except HTTPError as http_err:
        print (f'An HTTP error occurred: {http_err}')
except Exception as err:
        print (f'An unknown error occurred: {err}')
else:
    print('Success!')

print (response.content)


response.encoding = 'utf-8'
print (response.text)

print (response.json())

headers = response.headers
server = response.headers['Server']

print (headers)
print (server)