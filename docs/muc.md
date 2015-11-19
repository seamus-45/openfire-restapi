Methods defined here:
---------------------

```python
__init__(self, host, secret, endpoint='/plugins/restapi/v1/chatrooms')
    :param host: Scheme://Host/ for API requests
    :param secret: Shared secret key for API requests
    :param endpoint: Endpoint for API requests

add_room(self, roomname, name, description, servicename='conference', subject=None, password=None, maxusers=0, persistent=True, public=True, registration=True, visiblejids=True, changesubject=False, anycaninvite=False, changenickname=True, logenabled=True, registerednickname=False, membersonly=False, moderated=False, broadcastroles=None, owners=None, admins=None, members=None, outcasts=None)
    Create a chat room
    
    :param roomname: The name/id of the room. Can only contains lowercase and alphanumeric characters
    :param name: Also the name of the room, but can contains non alphanumeric characters
    :param description: Description text of the room
    :param servicename: (optional) The name of the Group Chat Service. Default: `conference`
    :param subject: (optional) Subject of the room
    :param password: (optional) The password that the user must provide to enter the room
    :param maxusers: (optional) The maximum number of occupants that can be simultaneously in the room. Default: 0 (unlimited)
    :param persistent: (optional) Persistent rooms are saved to the database to make their configurations persistent together with the affiliation of the users. Otherwise the room will be destroyed if the last occupant leave the room. Default: True
    :param public: (optional) True if the room is searchable and visible through service discovery. Default: True
    :param registration: (optional) True if users are allowed to register with the room. Default: True
    :param visiblejids: (optional) True if every presence packet will include the JID of every occupant. Default: True
    :param changesubject: (optional) True if participants are allowed to change the room’s subject. Default: True
    :param anycaninvite: (optional) True if occupants can invite other users to the room. Affects on members only rooms. Default: False
    :param changenickname: (optional) True if room occupants are allowed to change their nicknames. Default: True
    :param logenabled: (optional) True if the room’s conversation is being logged. Default: True
    :param registerednickname: (optional) True if registered users can only join the room using their registered nickname. Default: False
    :param membersonly: (optional) True if the room requires an invitation to enter. Default: False
    :param moderated: (optional) True if the room in which only those with “voice” may send messages to all occupants. Default: False
    :param broadcastroles: (optional) The list of roles of which presence will be broadcasted to the rest of the occupants.
    :type broadcastroles: List of strings. E.g. any from [ 'moderator', 'participant', 'visitor' ]
    :param owners: (optional) A collection with the current list of owners
    :type owners: List of strings. E.g. ['owner@localhost',]
    :param admins: (optional) A collection with the current list of admins
    :type admins: List of strings. E.g. ['admin@localhost',]
    :param members: (optional) A collection with the current list of room members. The collection contains the bareJID of the users with member affiliation. If the room is not members-only then the list will contain the users that registered with the room and therefore they may have reserved a nickname
    :type members: List of strings. E.g. ['member@localhost',]
    :param outcasts: (optional) A collection with the current list of outcast users. An outcast user is not allowed to join the room again
    :type outcasts: List of strings. E.g. ['outcast@localhost',]

delete_room(self, roomname, servicename='conference')
    Delete a chat room
    
    :param roomname: Exact room name
    :param servicename: (optional) The name of the Group Chat Service. Default: `conference`

get_room(self, roomname, servicename='conference')
    Retrieve exact chat room info
    
    :param roomname: The exact chat room name for request
    :param servicename: (optional) The name of the Group Chat Service. Default: `conference`

get_room_users(self, roomname, servicename='conference')
    Retrieve chat room participants
    
    :param roomname: The exact chat room name for request
    :param servicename: (optional) The name of the Group Chat Service. Default: `conference`

get_rooms(self, servicename='conference', typeof='public', query=None)
    Retrieve all chat rooms or filter by chat room name
    
    :param servicename: (optional) The name of the Group Chat Service. Default: `conference`
    :param typeof: (optional) Search only specified type of the rooms. Values: `all`, `public`. Default: `puclic`
    :param query: (optional) Search/Filter by room name. This act like the wildcard search %String%

grant_user_role(self, roomname, username, role, servicename='conference')
    Grant role to chat room user
    
    :param roomname: The exact chat room name for request
    :param username: The local username or the user JID
    :param role: Any from `owners`,`admins`,`members`,`outcasts`
    :param servicename: (optional) The name of the Group Chat Service. Default: `conference`

revoke_user_role(self, roomname, username, role, servicename='conference')
    Revoke role from chat room user
    
    :param roomname: The exact chat room name for request
    :param username: The local username or the user JID
    :param role: Any from `owners`,`admins`,`members`,`outcasts`
    :param servicename: (optional) The name of the Group Chat Service. Default: `conference`

update_room(self, roomname, name=None, description=None, servicename='conference', subject=None, password=None, maxusers=0, persistent=True, public=True, registration=True, visiblejids=True, changesubject=False, anycaninvite=False, changenickname=True, logenabled=True, registerednickname=False, membersonly=False, moderated=False, broadcastroles=None, owners=None, admins=None, members=None, outcasts=None)
    Update a chat room
    
    :param roomname: The name/id of the room. Can only contains lowercase and alphanumeric characters
    :param name: (optional) Also the name of the room, but can contains non alphanumeric characters
    :param description: (optional) Description text of the room
    :param servicename: (optional) The name of the Group Chat Service. Default: `conference`
    :param subject: (optional) Subject of the room
    :param password: (optional) The password that the user must provide to enter the room
    :param maxusers: (optional) The maximum number of occupants that can be simultaneously in the room. Default: 0 (unlimited)
    :param persistent: (optional) Persistent rooms are saved to the database to make their configurations persistent together with the affiliation of the users. Otherwise the room will be destroyed if the last occupant leave the room. Default: True
    :param public: (optional) True if the room is searchable and visible through service discovery. Default: True
    :param registration: (optional) True if users are allowed to register with the room. Default: True
    :param visiblejids: (optional) True if every presence packet will include the JID of every occupant. Default: True
    :param changesubject: (optional) True if participants are allowed to change the room’s subject. Default: True
    :param anycaninvite: (optional) True if occupants can invite other users to the room. Affects on members only rooms. Default: False
    :param changenickname: (optional) True if room occupants are allowed to change their nicknames. Default: True
    :param logenabled: (optional) True if the room’s conversation is being logged. Default: True
    :param registerednickname: (optional) True if registered users can only join the room using their registered nickname. Default: False
    :param membersonly: (optional) True if the room requires an invitation to enter. Default: False
    :param moderated: (optional) True if the room in which only those with “voice” may send messages to all occupants. Default: False
    :param broadcastroles: (optional) The list of roles of which presence will be broadcasted to the rest of the occupants.
    :type broadcastroles: List of strings. E.g. any from [ 'moderator', 'participant', 'visitor' ]
    :param owners: (optional) A collection with the current list of owners
    :type owners: List of strings. E.g. ['owner@localhost',]
    :param admins: (optional) A collection with the current list of admins
    :type admins: List of strings. E.g. ['admin@localhost',]
    :param members: (optional) A collection with the current list of room members. The collection contains the bareJID of the users with member affiliation. If the room is not members-only then the list will contain the users that registered with the room and therefore they may have reserved a nickname
    :type members: List of strings. E.g. ['member@localhost',]
    :param outcasts: (optional) A collection with the current list of outcast users. An outcast user is not allowed to join the room again
    :type outcasts: List of strings. E.g. ['outcast@localhost',]
```
