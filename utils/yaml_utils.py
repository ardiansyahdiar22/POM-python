import yaml

class YAMLUtils:
    @staticmethod
    def load_yaml(file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data

    @staticmethod
    def get(data, key):
        keys = key.split('/')
        result = data
        for k in keys:
            result = result.get(k, {})
        return result
