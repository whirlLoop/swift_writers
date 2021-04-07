"""Initial order.
    """


class InitialOrder():

    def __init__(self, user):
        if not user or user.isspace():
            raise ValueError('User should not be empty')
        self.user = user

    def academic_level(self, academic_level):
        self._academic_level = academic_level
        return self

    def essay(self, essay):
        self._essay = essay
        return self

    def due_date(self, due_date):
        self._due_date = due_date
        return self

    def total_cost(self, total_cost):
        self._total_cost = total_cost
        return self

    def pages(self, pages):
        self._pages = pages
        return self

    def __str__(self) -> str:
        return self.user
