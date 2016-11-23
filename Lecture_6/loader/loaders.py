import json
import yaml

from .base import Loader


class JSONLoader(Loader):
    def load(self):
        with open(self.filename) as f:
            input_data = json.load(f)
            return input_data


class YAMLLoader(Loader):
    def load(self):
        with open(self.filename) as f:
            input_data = yaml.load(f)
            return input_data
