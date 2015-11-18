Methods defined here:
---------------------

```python
__init__(self, host, secret, endpoint='/plugins/restapi/v1/users')
    :param host: Scheme://Host/ for API requests
    :param secret: Shared secret key for API requests
    :param endpoint: Endpoint for API requests

add_user(self, username, password, name=None, email=None)
    Add user
    
    :param username: The user name
    :param password: The password of the user
    :param name: (optional) The display name of the user
    :param email: (optional) The email address of the user

add_user_groups(self, username, groups)
    Add user to one or more groups
    
    :param username: The user name
    :param groups: One or more groups to be added in
    :type groups: List of strings. E.g. ['Admins','Friends']

add_user_roster_item(self, username, jid, name=None, subscription=None, groups=None)
    Add a user roster entry
    
    :param username: The user name
    :param jid: The JID of the roster item to be added. E.g. foo@example.org
    :param name: (optional) The nickname for the user when used in this roster
    :param subscription: (optional) The subscription type. One of SUBSCRIPTION_REMOVE,SUBSCRIPTION_NONE,SUBSCRIPTION_TO,SUBSCRIPTION_FROM,SUBSCRIPTION_BOTH
    :param groups: (optional) A list of groups to organize roster entries under
    :type groups: List of strings. E.g. ['Admins','Friends']

delete_user(self, username)
    Delete user
    
    :param username: The user name

delete_user_groups(self, username, groups)
    Remove user from one or more groups
    
    :param username: The user name
    :param groups: One or more groups to be removed from
    :type groups: List of strings. E.g. ['Admins','Friends']

delete_user_roster_item(self, username, jid)
    Delete a user roster entry
    
    :param username: The user name
    :param jid: The JID of the roster item to be deleted. E.g. foo@example.org

get_user(self, username)
    Retrieve exact user info
    
    :param username: The exact user name for request

get_user_groups(self, username)
    Retrieve all user groups
    
    :param username: The user name

get_user_roster(self, username)
    Retrieve user roster
    
    :param username: The user name

get_users(self, query=None)
    Retrieve all users or filter by user name
    
    :param query: (optional) Search/Filter by user name. This act like the wildcard search %String%

lock_user(self, username)
    Lockout a user
    
    :param username: The user name

unlock_user(self, username)
    Unlock a user
    
    :param username: The user name

update_user(self, username, newusername=None, password=None, name=None, email=None)
    Update user.
    
    :param username: The user name
    :param newusername: (optional) The new user name of the user
    :param password: (optional) The new password of the user
    :param name: (optional) The new display name of the user
    :param email: (optional) The new email address of the user

update_user_roster_item(self, username, jid, name=None, subscription=None, groups=None)
    Update a user roster entry
    
    :param username: The user name
    :param jid: The JID of the roster item to be updated. E.g. foo@example.org
    :param name: (optional) The nickname for the user when used in this roster
    :param subscription: (optional) The subscription type. One of SUBSCRIPTION_REMOVE,SUBSCRIPTION_NONE,SUBSCRIPTION_TO,SUBSCRIPTION_FROM,SUBSCRIPTION_BOTH
    :param groups: (optional) A list of groups to organize roster entries under
    :type groups: List of strings. E.g. ['Admins','Friends']
```

Data and other attributes defined here:
---------------------------------------

```python
SUBSCRIPTION_BOTH = 3

SUBSCRIPTION_FROM = 2

SUBSCRIPTION_NONE = 0

SUBSCRIPTION_REMOVE = -1

SUBSCRIPTION_TO = 1
```
