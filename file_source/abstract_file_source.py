class abstract_file_source(object):

    def __init__(self, destination):
        """init file source with root node destination"""
        
        raise Exception ("not implemented")

    def list_content(self, basedir=None):
        """list content in basedir"""
        
        raise Exception ("not implemented")

    def walk_content(self, basedir=None):
        """walk content from basedir"""
        
        raise Exception ("not implemented")
    
    def get_meta_data(self, target, verbose=False):
        """get meta data dictionary from given target"""
    
        raise Exception ("not implemented")
        
    def get_file_handler(self, offset=0):
        """get a file handler with offset"""
        
        raise Exception ("not implemented")
        
if __name__ == '__main__':
    
    share = abstract_file_source("/home")
    print share.list_content("/tmp")
    print share.walk_content("/tmp")


