from textnode import TextNode, TextType

def main():
    text_node = TextNode('Hello, World!', TextType.TEXT)
    print(text_node)
    text_node = TextNode('Hello, World!', TextType.ITALIC, 'https://www.google.com')
    print(text_node)
    text_node = TextNode('Hello, World!', TextType.CODE, 'https://www.google.com')
    print(text_node)
    text_node = TextNode('Hello, World!', TextType.BOLD, 'https://www.google.com')
    text_node2 = TextNode('Hello, World!', TextType.BOLD, 'https://www.google.com')
    print(text_node == text_node2)

main()