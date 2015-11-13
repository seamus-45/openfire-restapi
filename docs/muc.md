Python Library Documentation: module muc
# __CLASSES__

base.Base(__builtin__.object)
    Muc

## class __Muc__
****************************************

### data
****************************************
### descriptors
****************************************
### methods
****************************************
#### def __add_room__((self, roomname, name, description, servicename, subject, password, maxusers, persistent, public, registration, visiblejids, changesubject, anycaninvite, changenickname, logenabled, registerednickname, membersonly, moderated, broadcastroles, owners, admins, members, outcasts), None, None, (conference, None, None, 0, True, True, True, True, False, False, True, True, False, False, False, None, None, None, None, None)):

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

#### def __delete_room__((self, roomname, servicename), None, None, (conference,)):

Delete a chat room

:param roomname: Exact room name
:param servicename: (optional) The name of the Group Chat Service. Default: `conference`

#### def __get_room__((self, roomname, servicename), None, None, (conference,)):

Retrieve exact chat room info

:param roomname: The exact chat room name for request
:param servicename: (optional) The name of the Group Chat Service. Default: `conference`

#### def __get_room_users__((self, roomname, servicename), None, None, (conference,)):

Retrieve chat room participants

:param roomname: The exact chat room name for request
:param servicename: (optional) The name of the Group Chat Service. Default: `conference`

#### def __get_rooms__((self, servicename, typeof, query), None, None, (conference, public, None)):

Retrieve all chat rooms or filter by chat room name

:param servicename: (optional) The name of the Group Chat Service. Default: `conference`
:param typeof: (optional) Only as List Room in Directory set rooms. Values: `all`, `public`. Default: `puclic`
:param query: (optional) Search/Filter by room name. This act like the wildcard search %String%

#### def __grant_user_role__((self, roomname, username, role, servicename), None, None, (conference,)):

Grant role to chat room user

:param roomname: The exact chat room name for request
:param username: The local username or the user JID
:param role: Any from `owners`,`admins`,`members`,`outcasts`
:param servicename: (optional) The name of the Group Chat Service. Default: `conference`

#### def __revoke_user_role__((self, roomname, username, role, servicename), None, None, (conference,)):

Revoke role from chat room user

:param roomname: The exact chat room name for request
:param username: The local username or the user JID
:param role: Any from `owners`,`admins`,`members`,`outcasts`
:param servicename: (optional) The name of the Group Chat Service. Default: `conference`

#### def __update_room__((self, roomname, name, description, servicename, subject, password, maxusers, persistent, public, registration, visiblejids, changesubject, anycaninvite, changenickname, logenabled, registerednickname, membersonly, moderated, broadcastroles, owners, admins, members, outcasts), None, None, (conference, None, None, 0, True, True, True, True, False, False, True, True, False, False, False, None, None, None, None, None)):

Update a chat room

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

