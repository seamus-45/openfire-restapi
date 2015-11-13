# Help on module groups:

__NAME__
--------
`groups - # -*- coding: utf-8 -*-`

__FILE__
--------
`/openfire-restapi/ofrestapi/groups.py`

__CLASSES__
-----------
```python
base.Base(__builtin__.object)
    Groups
```

class Groups(base.Base)
-----------------------
    Method resolution order:
```python
Groups
base.Base
__builtin__.object
```
    
Methods defined here:
---------------------

```python
__init__(self, host, secret, endpoint='/plugins/restapi/v1/groups')
    :param host: Scheme://Host/ for API requests
    :param secret: Shared secret key for API request
    :param endpoint: Endpoint for API request

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

Data descriptors inherited from base.Base:
------------------------------------------

```python
__dict__
    dictionary for instance variables (if defined)

__weakref__
    list of weak references to the object (if defined)
```


