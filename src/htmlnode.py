class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_to_string = ""
        if(self.props == None):
            return props_to_string

        for prop in self.props:
            props_to_string += (f' {prop}="{self.props[prop]}"')
        return props_to_string
    
    def __repr__(self):
       return(
            f"HTMLNode(Tag: {self.tag} " +
            f"Value: {self.value} " +
            f"Children: {self.children} " +
            f"Props: {self.props})"
       )
    
