Methods defined here:
---------------------

```python
__init__(self, host, secret, endpoint='/plugins/restapi/v1/system/properties')
    :param host: Scheme://Host/ for API requests
    :param secret: Shared secret key for API requests
    :param endpoint: Endpoint for API requests

delete_prop(self, key)
    Delete a system property
    
    :param key: The name of system property

get_concurrent_sessions(self)
    Retrieve concurrent sessions

get_prop(self, key)
    Retrieve system property
    
    :param key: The name of system property

get_props(self)
    Retrieve all system properties

update_prop(self, key, value)
    Create or update a system property
    
    :param key: The name of system property
    :param value: The value of system property
```
