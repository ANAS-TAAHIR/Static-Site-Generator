import unittest

from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_text_node(self):
        text_node = TextNode('Hello, World!', 'text')
        self.assertEqual(text_node, TextNode('Hello, World!', TextType.TEXT))
        text_node = TextNode('Hello, World!', 'italic', 'https://www.google.com')
        self.assertEqual(text_node, TextNode('Hello, World!', TextType.ITALIC, 'https://www.google.com'))
        text_node = TextNode('Hello, World!', 'code', 'https://www.google.com')
        self.assertEqual(text_node, TextNode('Hello, World!', TextType.CODE, 'https://www.google.com'))
        text_node = TextNode('Hello, World!', 'bold', 'https://www.google.com')
        text_node2 = TextNode('Hello, World!', 'wrong', 'https://www.google.com')
        self.assertFalse(text_node == text_node2)
        text_node = TextNode("This is a text node", TextType.BOLD, "evil.com")
        text_node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(text_node, text_node2)

if __name__ == '__main__':
    unittest.main()