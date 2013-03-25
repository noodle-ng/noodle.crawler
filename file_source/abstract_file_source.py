class abstract_file_source:

    def __init__(self, destination):
        """init file source with root node destination"""
        
        print("not implemented")
        raise

    def walk_from(self, target=None, recursive=False):
        """walk from target node (os.walk like)"""
        
        print("not implemented")
        raise
    
    def get_meta_data(self, target, verbose=False):
        """get meta data dictionary from given target"""
    
        print("not implemented")
        raise
        
    def get_file_handler(self, offset=0):
        """get a file handler with offset"""
        
        print("not implemented")
        raise

