# -*- coding: utf-8 -*-
""""""

class AbstractFileSource(object):
    """"""

    def __init__(self, destination):
        """init file source with root node destination"""
        raise NotImplementedError()

    def walk_from(self, target=None, recursive=False):
        """walk from target node (os.walk like)"""
        raise NotImplementedError()

    def get_meta_data(self, target, verbose=False):
        """get meta data dictionary from given target"""
        raise NotImplementedError()

    def get_file_handler(self, offset=0):
        """get a file handler with offset"""
        raise NotImplementedError()

if __name__ == '__main__':

    burning_house = AbstractFileSource(None)

