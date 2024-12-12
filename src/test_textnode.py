import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_same_content(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_with_optional_url(self):
        node1 = TextNode("This is a text node", TextType.LINK, "abc.com")
        node2 = TextNode("This is a text node", TextType.LINK, "abc.com")
        self.assertEqual(node1, node2)

    def test_eq_special_characters(self):
        node1 = TextNode("This is a(){} text node", TextType.CODE, "abc.com")
        node2 = TextNode("This is a(){} text node", TextType.CODE, "abc.com")
        self.assertEqual(node1, node2)

    def test_not_eq_different_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "evil.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_content(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text nosde", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_repr_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_repr_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "abc.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, link, abc.com)")

    def test_repr_special_characters(self):
        node = TextNode("This is a(){} text node", TextType.CODE, "abc.com")
        self.assertEqual(repr(node), "TextNode(This is a(){} text node, code, abc.com)")

    def test_false_comparison_different_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertFalse(node1 == node2)

    def test_false_comparison_different_content(self):
        node1 = TextNode("This is a text node 2", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertFalse(node1 == node2)

    def test_empty_content(self):
        node1 = TextNode("", TextType.TEXT)
        node2 = TextNode("", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_url_only_in_one_node(self):
        node1 = TextNode("This is a text node", TextType.LINK, "abc.com")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_type_and_url_differ(self):
        node1 = TextNode("This is a text node", TextType.LINK, "abc.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "abc.com")
        self.assertNotEqual(node1, node2)

    def test_empty_url_comparison(self):
        node1 = TextNode("This is a text node", TextType.LINK, "")
        node2 = TextNode("This is a text node", TextType.LINK, None)
        self.assertNotEqual(node1, node2)

    def test_eq_with_leading_and_trailing_spaces(self):
        node1 = TextNode(" This is a text node ", TextType.TEXT)
        node2 = TextNode(" This is a text node ", TextType.TEXT)
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
