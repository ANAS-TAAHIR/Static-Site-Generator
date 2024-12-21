from typing import List, Dict


class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: List["HTMLNode"] = None,
        props: Dict[str, str] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def __repr__(self):
        return f"{self.tag}({self.value}, {self.children}, {self.props})"

    def to_html(self) -> str:
        raise NotImplementedError()

    def props_to_html(self) -> str:
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
