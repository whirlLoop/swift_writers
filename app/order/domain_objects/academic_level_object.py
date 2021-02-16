"""AcademicLevel popo
    """


class AcademicLevelObject():

    def __init__(self, name, base_price) -> None:
        self.name = name
        self.base_price = base_price

    def __str__(self) -> str:
        return self.name
