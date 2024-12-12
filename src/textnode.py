from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGES = "images"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        if text_type in TextType.__members__:
            self.type = TextType(text_type)
        else:
            raise ValueError("Invalid text type")
        print(self.type)
        self.url = url

    def __eq__(self, value):
        return (
            self.text == value.text
            and self.type == value.type
            and self.url == value.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
