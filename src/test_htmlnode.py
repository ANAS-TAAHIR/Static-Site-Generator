import unittest

from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Click here.",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(), 'href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html2(self):
        node = HTMLNode(
            None, None, None, {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(), 'href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html3(self):
        node = HTMLNode(
            None,
            None,
            None,
            {"src": "string representing source text", "height": "500px"},
        )
        self.assertEqual(
            node.props_to_html(),
            'src="string representing source text" height="500px"',
        )


class TestLeafNode(unittest.TestCase):
    def test_leafNode_to_html(self):
        node = LeafNode(
            "a", "Click here.", {"href": "https://www.google.com", "target": "_blank"}
        )
        print(node.to_html())
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com" target="_blank">Click here.</a>',
        )

    def test_leafNode_to_html2(self):
        node = LeafNode(
            None, "Click here.", {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node.to_html(), "Click here.")
