from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if(self.tag == None):
            raise ValueError("Tag not set for ParentNode")
        if(self.children == None):
            raise ValueError("Children not set for ParentNode")
        
        children_to_html = ""
        for child in self.children:
            children_to_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_to_html}</{self.tag}>"
        


