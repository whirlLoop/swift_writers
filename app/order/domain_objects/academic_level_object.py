"""AcademicLevel popo
    """


class AcademicLevelObject():

    def __init__(self, academic_level_name, academic_level_display_name, base_price) -> None:
        self.academic_level_name = academic_level_name
        self.academic_level_display_name = academic_level_display_name
        self.base_price = base_price

    def __str__(self) -> str:
        return self.academic_level_display_name
