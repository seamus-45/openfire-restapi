Python Library Documentation: module users
# __CLASSES__

base.Base(__builtin__.object)
    Users

## class __Users__
****************************************

### data
****************************************
```
__SUBSCRIPTION_BOTH__ = 3
__SUBSCRIPTION_FROM__ = 2
__SUBSCRIPTION_NONE__ = 0
__SUBSCRIPTION_REMOVE__ = -1
__SUBSCRIPTION_TO__ = 1
```
### methods
****************************************
#### def __add_user__((self, username, password, name, email), None, None, (None, None)):

Add user

```
:param username: The user name
:param password: The password of the user
:param name: (optional) The display name of the user
:param email: (optional) The email address of the user
```

#### def __add_user_groups__((self, username, groups), None, None, None):

Add user to one or more groups

```
:param username: The user name
:param groups: One or more groups to be added in
:type groups: List of strings. E.g. ['Admins','Friends']
```

#### def __add_user_roster_item__((self, username, jid, name, subscription, groups), None, None, (None, None, None)):

Add a user roster entry

```
:param username: The user name
:param jid: The JID of the roster item to be added. E.g. foo@example.org
:param name: (optional) The nickname for the user when used in this roster
:param subscription: (optional) The subscription type. One of SUBSCRIPTION_REMOVE, SUBSCRIPTION_NONE,SUBSCRIPTION_TO,SUBSCRIPTION_FROM,SUBSCRIPTION_BOTH
:param groups: (optional) A list of groups to organize roster entries under
:type groups: List of strings. E.g. ['Admins','Friends']
```

#### def __delete_user__((self, username), None, None, None):

Delete user

```
:param username: The user name
```

#### def __delete_user_groups__((self, username, groups), None, None, None):

Remove user from one or more groups

```
:param username: The user name
:param groups: One or more groups to be removed from
:type groups: List of strings. E.g. ['Admins','Friends']
```

#### def __delete_user_roster_item__((self, username, jid), None, None, None):

Delete a user roster entry

```
:param username: The user name
:param jid: The JID of the roster item to be deleted. E.g. foo@example.org
```

#### def __get_user__((self, username), None, None, None):

Retrieve exact user info

```
:param username: The exact user name for request
```

#### def __get_user_groups__((self, username), None, None, None):

Retrieve all user groups

```
:param username: The user name
```

#### def __get_user_roster__((self, username), None, None, None):

Retrieve user roster

```
:param username: The user name
```

#### def __get_users__((self, query), None, None, (None,)):

Retrieve all users or filter by user name

```
:param query: (optional) Search/Filter by user name. This act like the wildcard search %String%
```

#### def __lock_user__((self, username), None, None, None):

Lockout a user

```
:param username: The user name
```

#### def __unlock_user__((self, username), None, None, None):

Unlock a user

```
:param username: The user name
```

#### def __update_user__((self, username, newusername, password, name, email), None, None, (None, None, None, None)):

Update user.

```
:param username: The user name
:param newusername: (optional) The new user name of the user
:param password: (optional) The new password of the user
:param name: (optional) The new display name of the user
:param email: (optional) The new email address of the user
```

#### def __update_user_roster_item__((self, username, jid, name, subscription, groups), None, None, (None, None, None)):

Update a user roster entry

```
:param username: The user name
:param jid: The JID of the roster item to be updated. E.g. foo@example.org
:param name: (optional) The nickname for the user when used in this roster
:param subscription: (optional) The subscription type. One of SUBSCRIPTION_REMOVE, SUBSCRIPTION_NONE,SUBSCRIPTION_TO,SUBSCRIPTION_FROM,SUBSCRIPTION_BOTH
:param groups: (optional) A list of groups to organize roster entries under
:type groups: List of strings. E.g. ['Admins','Friends']
```
