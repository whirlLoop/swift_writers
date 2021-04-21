import json
from order.domain_objects.discipline import Discipline
from order.DAOs.base_dao import BaseDAO


class DisciplineDAO(BaseDAO):
    """Returns a list of disciplines.
    """

    def __init__(self):
        super().__init__()
        self.get_disciplines()

    def get_disciplines(self):
        disciplines = []
        if self.cache.get("disciplines"):
            disciplines = json.loads((self.cache.get("disciplines")))
        for discipline in disciplines:
            discipline_object = Discipline(
                discipline['id']
            ).discipline_name(discipline['discipline_name']).\
                discipline_category(discipline['discipline_category'])
            self.objects.append(discipline_object)
