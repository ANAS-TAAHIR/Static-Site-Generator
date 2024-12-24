from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


def text_node_to_html_node(text_node):
    if text_node.type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.type == TextType.LINK:
        if not text_node.url:
            raise ValueError("URL is required for links")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("URL is required for images")
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Invalid text type")


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        if text_type in TextType:
            self.type = TextType(text_type)
        else:
            raise ValueError("Invalid text type")
        self.url = url

    def __eq__(self, value):
        return (
            self.text == value.text
            and self.type == value.type
            and self.url == value.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
