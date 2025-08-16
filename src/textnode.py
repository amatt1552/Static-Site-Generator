from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = ""
    BOLD_TEXT = "**"
    ITALIC_TEXT = "_"
    CODE_TEXT = "`"
    LINK = "["
    IMAGE = "!"

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        text_match = self.text == other.text
        type_match = self.text_type == other.text_type
        url_match = self.url == other.url
        return text_match and type_match and url_match

    def __repr__ (self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

