# OAUTH 2.0

One if the libraries that enables Python to perform authenticating with a third-party server via OAUTH 2.0 is: ```requests-oauthlib```.

Install it (int he evnironment) with:

```bash
pip install requests_oauthlib
```

<br>

## Web Application Flow

At minimum, the **Authorization-Flow** requires set of ```client-id``` and ```client-secret``` to be able to authentication the *Client* on the *Identity Provider Server*.<br>
In addition the Client should register its ```redirect-url``` which the Identity server will use to pass the ```authorization-code```.

There are few parameters such as ```scope``` and ```state``` that the Client might need to send to Server if required.

The Client should also have The urls of ```authorization``` and ```access token``` endpoints. The ```refresh token``` endpoint is usually the same as access token.

The overall config to use the authentication server is as follows (but it can vary based on the different server configuration):

```py
from requests_oauthlib import OAuth2Session

# example
auth_endpoint = 'https://login.salesforce.com/services/oauth2/authorize'
token_endpoint = 'https://login.salesforce.com/services/oauth2/token'

client_id = '6G7mZMY4ozS8O4FBSxAq'
client_secret = '6G7mZMY4ozS8O4FBSxAq6G7mZMY4ozS8O4FBSxAq6G7mZMY4ozS8O4FBSxAq'
redirect_url = ''

scope = 'profile'

oauth = OAuth2Session(client_id, 
                        redirect_uri=redirect_uri,
                        scope=scope)

authorization_url, state = oauth.authorization_url(auth_endpoint)

redirect_response = raw_input(redirect_url)

oauth.fetch_token(token_url,
                client_secret=client_secret,
                authorization_response=redirect_response)
```

From this point the ```auth``` object should be ready to be used in requests which requires authentication.

```py
getCars  = oauth.get('https://wwww.example.com/makes')
cars = getCars.content
```

<br>

### References

* [Requests-OAuthlib - OAuth 2 Workflow](https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html)