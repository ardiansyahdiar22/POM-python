from utils.yaml_utils import YAMLUtils

class SelectorHelper:
    def __init__(self):
        self.selectors = YAMLUtils.load_yaml('./selector/selectors.yml')
    
    def get_selector(self, selector_key):
        return self.selectors.get(selector_key)