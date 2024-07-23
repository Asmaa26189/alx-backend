#!/usr/bin/env python3
"""BaseCaching"""


class BaseCaching():
    """BaseCaching"""
    MAX_ITEMS = 4

    def __init__(self):
        """Initiliazes"""
        self.cache_data = {}

    def print_cache(self):
        """Prints """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """put"""
        error_msg = "put must be implemented in your cache class"
        raise NotImplementedError(error_msg)

    def get(self, key):
        """get"""
        error_msg = "get must be implemented in your cache class"
        raise NotImplementedError(error_msg)