import unittest

from inline import *


class TestSplitNodesDelimiter(unittest.TestCase):
    def test1(self):
        node = TextNode("This is` text with a` code block word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            str(result),
            "[TextNode(This is, text, None), TextNode( text with a, code, None), TextNode( code block word, text, None)]",
        )

    def test2(self):
        node = TextNode("`This is` text with a code block word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            str(result),
            "[TextNode(This is, code, None), TextNode( text with a code block word, text, None)]",
        )

    def test3(self):
        node = TextNode("`This is` text with a code block word", TextType.TEXT)
        node2 = TextNode(
            "This is text with a **bolded phrase** in the middle", TextType.TEXT
        )
        result = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        # print(result)
        self.assertEqual(
            str(result),
            "[TextNode(`This is` text with a code block word, text, None), TextNode(This is text with a , text, None), TextNode(bolded phrase, bold, None), TextNode( in the middle, text, None)]",
        )

    def test4(self):
        node = TextNode("`This is` text with a code block word", TextType.TEXT)
        node2 = TextNode(
            "This is text with a **bolded phrase** in the middle", TextType.TEXT
        )
        result = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        # print(result)
        self.assertEqual(
            str(result),
            "[TextNode(This is, code, None), TextNode( text with a code block word, text, None), TextNode(This is text with a **bolded phrase** in the middle, text, None)]",
        )

    def test5(self):
        node = TextNode(
            "This is code block: `code here``more code here`", TextType.TEXT
        )
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        # print(result)
        self.assertEqual(
            str(result),
            "[TextNode(This is code block: , text, None), TextNode(code here, code, None), TextNode(more code here, code, None)]",
        )
