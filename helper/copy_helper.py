from utils.yaml_utils import YAMLUtils

class HelpergetCopy:
    def __init__(self):
        self.copy = YAMLUtils.load_yaml('./selector/credentials_and_copy.yml')
    
    def get_copy(self, user_key):
        return self.copy.get(user_key)