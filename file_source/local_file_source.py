from abstract_file_source import abstract_file_source 
import os

class local_file_source(abstract_file_source):

    def __init__(self, destination):
        """init file source with root node destination"""
        
        self.root = destination

    def list_content(self, basedir=None):
        """list content in basedir"""
        
        if basedir == None:
            basedir = self.root
        
        os.chdir(basedir)
        entries = os.listdir(basedir)
        
        files = filter(os.path.isfile, entries) 
        folders = filter(os.path.isdir, entries)
        
        return basedir, folders, files

    def walk_content(self, basedir=None):
        """walk content from basedir"""
        
        if basedir == None:
            basedir = self.root
        
        return list(os.walk(basedir))
    
    def get_meta_data(self, target, verbose=False):
        """get meta data dictionary from given target"""
    
        raise Exception ("not implemented")
        
    def get_file_handler(self, offset=0):
        """get a file handler with offset"""
        
        raise Exception ("not implemented")
        
if __name__ == '__main__':
    
    share = local_file_source("/home")
    print share.list_content("/tmp")
    print share.walk_content("/tmp")

