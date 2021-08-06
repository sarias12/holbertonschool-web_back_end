#!/usr/bin/env python3
"""
Module for  manage the API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[summary]

        Args:
            path (str)
            excluded_paths (List[str])

        Returns:
            bool
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Flask request object - Authorization Header

        Args:
            request: Defaults to None.

        Returns:
            str
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object - Current User

        Returns:
            User
        """
        return None
