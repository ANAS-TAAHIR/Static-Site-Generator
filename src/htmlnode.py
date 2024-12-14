from typing import List, Dict


class HTMLNode:
    def __init__(self, tag:str=None , value:str=None, children:List['HTMLNode']=None, props:Dict[str, str]=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}
    
    def __repr__(self):
        return f'{self.tag}({self.value}, {self.children}, {self.props})'

    def to_html(self) -> str:
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])