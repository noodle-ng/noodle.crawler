class abstract_file_source:

    def __init__(self, destination):
        """init file source with root node destination"""
        
        raise Exception ("not implemented")

    def walk_from(self, target=None, recursive=False):
        """walk from target node (os.walk like)"""
        
        raise Exception ("not implemented")
    
    def get_meta_data(self, target, verbose=False):
        """get meta data dictionary from given target"""
    
        raise Exception ("not implemented")
        
    def get_file_handler(self, offset=0):
        """get a file handler with offset"""
        
        raise Exception ("not implemented")
        
if __name__ == '__main__':
    
    burning_house = abstract_file_source(None)

