#!/usr/bin/python3
"""Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching System

    Args:
        BaseCaching (Class): Parent class
    """

    def put(self, key, item):
        """Add item in the cache

        Args:
            key (str): value for item
            item (str): item for dictionary
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """Get a item by key

        Args:
            key (str): key for get value from cache data dictionary

        Returns:
            Value of key (str):  value from cache data or None
        """
        if (key in self.cache_data and key is not None):
            return self.cache_data[key]
        return None
