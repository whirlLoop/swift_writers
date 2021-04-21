"""Discipline object.
    """


class Discipline():

    def __init__(self, discipline_id):
        """Creates an instance of the student's branch of knowledge.

        Args:
            discipline_id (int): the discipline_id of the discipline e.g 7.

        Raises:
            ValueError: error raised if no value is discipline id.
        """
        if not discipline_id or discipline_id is None:
            raise ValueError(
                'Please provide the discipline id.')
        self.discipline_id = discipline_id

    def discipline_category(self, discipline_category):
        self._discipline_category = discipline_category
        return self

    def discipline_name(self, discipline_name):
        self._discipline_name = discipline_name
        return self

    def __str__(self) -> str:
        return self._discipline_name
