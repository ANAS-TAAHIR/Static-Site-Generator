from textnode import TextNode, TextType

def main():
    text_node = TextNode('Hello, World!', 'text')
    print(text_node)
    text_node = TextNode('Hello, World!', 'italic', 'https://www.google.com')
    print(text_node)
    text_node = TextNode('Hello, World!', 'code', 'https://www.google.com')
    print(text_node)
    text_node = TextNode('Hello, World!', 'bold', 'https://www.google.com')
    text_node2 = TextNode('Hello, World!', 'wrong', 'https://www.google.com')
    print(text_node == text_node2)

main()