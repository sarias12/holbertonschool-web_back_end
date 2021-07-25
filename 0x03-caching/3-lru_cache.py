#!/usr/bin/python3
""" LRU caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU

    Args:
        BaseCaching (class): Parent class
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.items = []

    def put(self, key, item):
        """Add item in the cache with LRU Algorithm

        Args:
            key (str): value for item
            item (str): item for dictionary
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.items.remove(key)
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discard = self.items.pop(0)
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
            self.items.remove(key)
            self.items.append(key)
            return self.cache_data[key]
        return None
