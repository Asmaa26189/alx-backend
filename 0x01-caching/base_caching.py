#!/usr/bin/python3
""" Base """


class BaseCaching():
    """ BaseCaching """
    MAX_ITEMS = 4

    def __init__(self):
        """ __init__"""
        self.cache_data = {}

    def print_cache(self):
        """ print_cache"""
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """PUT"""
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """GET"""
        raise NotImplementedError("get must be implemented in your cache class")