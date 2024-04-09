#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    prevent the user from creating new lockedclass attributes
    for everything but attribute called 'first_name'
    """

    __slots__ = ["first_name"]
