class abstract_file_source:

    def __init__(self, destination):
        """init file source with root node destination"""
        
        pass

    def walk_from(self, target=None, recursive=False):
        """walk from target node (os.walk like)"""
        
        pass
    
    def get_meta_data(self, target, verbose=False):
        """get meta data dictionary from given target"""
    
        pass
        
    def get_file_handler(self, offset=0):
        """get a file handler with offset"""
        
        pass
        

