"""Essay popo
"""


class EssayObject():

    def __init__(self, essay_name, essay_display_name, price_per_page) -> None:
        self.essay_name = essay_name
        self.essay_display_name = essay_display_name
        self.price_per_page = price_per_page

    def __str__(self) -> str:
        return self.essay_display_name
