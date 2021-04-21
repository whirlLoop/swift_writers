"""Reads essay data from file
    """
import json


class DataFromFile():

    def __init__(self) -> None:
        self.essays = json.dumps(
            self.get_data_from_file('order/data/essays.json'))
        self.academic_levels = json.dumps(self.get_data_from_file(
            'order/data/academic_levels.json'))
        self.disciplines = json.dumps(self.get_data_from_file(
            'order/data/disciplines.json'))

    def get_data_from_file(self, filename):
        try:
            opened_file = open(filename)
        except IOError as exception:
            # log exception
            print(exception)
            return []
        with opened_file:
            data = json.loads(opened_file.read())
        return data

    def get(self, key):
        return getattr(self, key)

    def delete(self, key):
        setattr(self, key, None)
