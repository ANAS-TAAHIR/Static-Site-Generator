import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test1(self):
        tn1 = TextNode("Slightly less serious test", "text")
        self.assertEqual(
            text_node_to_html_node(tn1).to_html(), "Slightly less serious test"
        )

    def test2(self):
        tn2 = TextNode("Second serious test", "bold")
        self.assertEqual(
            text_node_to_html_node(tn2).to_html(), "<b>Second serious test</b>"
        )

    def test3(self):
        with self.assertRaises(ValueError):
            tn2 = TextNode("Second serious test", "lilatic")

    def test4(self):
        tn3 = TextNode("Third serious test", "italic")
        self.assertEqual(
            text_node_to_html_node(tn3).to_html(), "<i>Third serious test</i>"
        )

    def test5(self):
        tn4 = TextNode("Fourth serious test", "code")
        self.assertEqual(
            text_node_to_html_node(tn4).to_html(), "<code>Fourth serious test</code>"
        )

    def test6(self):
        tn5 = TextNode("Fifth serious test", "image", "obrazek.com")
        self.assertEqual(
            text_node_to_html_node(tn5).to_html(),
            '<img src="obrazek.com" alt="Fifth serious test">',
        )



if __name__ == "__main__":
    unittest.main()
