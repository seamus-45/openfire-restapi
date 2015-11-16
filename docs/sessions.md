Methods defined here:
---------------------

```python
__init__(self, host, secret, endpoint='/plugins/restapi/v1/sessions')
    :param host: Scheme://Host/ for API requests
    :param secret: Shared secret key for API requests
    :param endpoint: Endpoint for API requests

close_user_sessions(self, username)
    Close sessions of exact user
    
    :param username: The user name

get_sessions(self)
    Retrieve sessions of all users

get_user_sessions(self, username)
    Retrieve sessions of exact user
    
    :param username: The user name
```
