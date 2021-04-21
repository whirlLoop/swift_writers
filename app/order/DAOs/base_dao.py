from order.DAOs.data_from_file import DataFromFile


class BaseDAO():

    def __init__(self):
        self.cache = DataFromFile()
        self.objects = []

    def __len__(self):
        return len(self.objects)

    def __iter__(self):
        for item in self.objects:
            yield item
