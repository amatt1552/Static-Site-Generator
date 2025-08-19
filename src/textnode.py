from enum import Enum
from src.leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"
    LINK = "["
    IMAGE = "!"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        text_match = self.text == other.text
        type_match = self.text_type == other.text_type
        url_match = self.url == other.url
        return text_match and type_match and url_match

    def __repr__ (self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    # TODO move function to seperate file.
    def to_html_node(self):
        match(self.text_type):
            case TextType.TEXT:
                return LeafNode(None, self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALIC:
                return LeafNode("i", self.text)
            case TextType.CODE:
                return LeafNode("code", self.text)
            case TextType.LINK:
                return LeafNode("a", self.text, {"href": self.url})
            case TextType.IMAGE:
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
            case _:
                raise Exception("Passed Text Type does not exist")
