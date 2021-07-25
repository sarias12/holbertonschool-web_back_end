#!/usr/bin/python3
""" FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO

    Args:
        BaseCaching (class): Parent class
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.items = []

    def put(self, key, item):
        """Add item in the cache with FIFO Algorithm

        Args:
            key (str): value for item
            item (str): item for dictionary
        """
        if (key is not None and item is not None):
            if (len(self.items) < self.MAX_ITEMS):
                self.items.append(key)
                self.cache_data[key] = item
            else:
                if(key not in self.cache_data):
                    discard = self.items.pop(0)
                    self.items.append(key)
                    self.cache_data.pop(discard)
                    self.cache_data[key] = item
                    print('DISCARD: ' + discard)

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
