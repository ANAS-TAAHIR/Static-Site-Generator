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


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
            continue
        matchesImage = extract_markdown_images(node.text)
        if not matchesImage:
            new_nodes.append(node)
            continue
        parts = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        for i, part in enumerate(parts):
            if i % 3 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            elif i % 3 == 1:
                new_nodes.append(TextNode(matchesImage.pop(0), TextType.IMAGE))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
            continue
        matchesLink = extract_markdown_links(node.text)
        if not matchesLink:
            new_nodes.append(node)
            continue
        parts = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        for i, part in enumerate(parts):
            if i % 3 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            elif i % 3 == 1:
                new_nodes.append(TextNode(matchesLink.pop(0), TextType.LINK))
    return new_nodes
