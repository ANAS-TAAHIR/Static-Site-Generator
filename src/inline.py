import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            if part:
                new_nodes.append(
                    TextNode(part, TextType.TEXT if i % 2 == 0 else text_type)
                )
    return new_nodes


def extract_markdown_images(text):
    matchesImage = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matchesImage


def extract_markdown_links(text):
    matchesLink = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matchesLink
