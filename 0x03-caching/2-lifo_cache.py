#!/usr/bin/python3
""" LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO

    Args:
        BaseCaching (class): Parent class
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.items = []

    def put(self, key, item):
        """Add item in the cache with LIFO Algorithm

        Args:
            key (str): value for item
            item (str): item for dictionary
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discard = self.items.pop()
                    self.cache_data.pop(discard)
                    print('DISCARD: ' + discard)
                self.cache_data[key] = item
            self.items.append(key)

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
