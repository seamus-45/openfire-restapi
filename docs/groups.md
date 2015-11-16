Methods defined here:
---------------------

```python
__init__(self, host, secret, endpoint='/plugins/restapi/v1/groups')
    :param host: Scheme://Host/ for API requests
    :param secret: Shared secret key for API requests
    :param endpoint: Endpoint for API requests

add_group(self, groupname, description)
    Create a group
    
    :param groupname: Name of the group
    :param description: Description of the group

delete_group(self, groupname)
    Delete a group
    
    :param groupname: The exact group name for request

get_group(self, groupname)
    Retrieve exact group info
    
    :param groupname: The exact group name for request

get_groups(self)
    Retrieve all groups

update_group(self, groupname, description)
    Update a group
    
    :param groupname: Name of the group
    :param description: Description of the group
```
