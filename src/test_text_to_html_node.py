import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from markdown_conversion import split_nodes_delimiter

class TestHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = TextNode.to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node") 

    def test_error(self):
        node = TextNode("wrong type?!", "link")
        try:
            html_node = TextNode.to_html_node(node)
            self.assertTrue(False)
        except Exception as e:
            self.assertTrue("Passed Text Type does not exist" in str(e))

    def test_to_html_code(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = TextNode.to_html_node(node)
        self.assertEqual(
            html_node.to_html(),
            "<b>This is a bold node</b>"
            )
        
        node = TextNode("this is a linked node", TextType.LINK, "https://www.google.com")
        html_node = TextNode.to_html_node(node)
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://www.google.com">this is a linked node</a>'
            )
        
        node = TextNode("this is an image node", TextType.IMAGE, "https://www.catfeet.com")
        html_node = TextNode.to_html_node(node)
        self.assertEqual(
            html_node.to_html(),
            '<img src="https://www.catfeet.com" alt="this is an image node"></img>'
            )

if __name__ == "__main__":
    unittest.main()