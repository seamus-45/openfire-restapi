Python Library Documentation: module groups

# __NAME__

groups - # -*- coding: utf-8 -*-

# __FILE__

/home/fedotov_sv/python-openfire/openfire/groups.py

# __CLASSES__

base.Base(__builtin__.object)
    Groups

## class __Groups__
****************************************

### data
****************************************
### descriptors
****************************************
### methods
****************************************
#### def __add_group__((self, groupname, description), None, None, None):

Create a group

:param groupname: Name of the group
:param description: Description of the group

#### def __delete_group__((self, groupname), None, None, None):

Delete a group

:param groupname: The exact group name for request

#### def __get_group__((self, groupname), None, None, None):

Retrieve exact group info

:param groupname: The exact group name for request

#### def __get_groups__((self,), None, None, None):

Retrieve all groups

#### def __update_group__((self, groupname, description), None, None, None):

Update a group

:param groupname: Name of the group
:param description: Description of the group

