import unittest
from src.htmlnode import HTMLNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "text here",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            }
         )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node_a = HTMLNode()
        node_b = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
            )
        
        tested_value_a = (
            "HTMLNode(Tag: None " +
            "Value: None " + 
            "Children: None " + 
            "Props: None)"
        )
        self.assertEqual(repr(node_a), tested_value_a)

        tested_value_b = (
            "HTMLNode(Tag: p " +
            "Value: What a strange world " + 
            "Children: None " + 
            "Props: {'class': 'primary'})"
        )
        self.assertEqual(repr(node_b), tested_value_b)


    def test_leaf_to_html(self):
        node_a = LeafNode(None, "Hello There!")
        self.assertEqual(node_a.to_html(), "Hello There!")

        node_b = LeafNode(None, "I have a link?", {"href":"https://www.google.com"})
        self.assertEqual(node_b.to_html(), "I have a link?")

        node_c = LeafNode("p", "Im a paragraph")
        self.assertEqual(node_c.to_html(), "<p>Im a paragraph</p>")

        node_d = LeafNode("p", "Im a paragraph with link", {"href":"https://www.google.com"})
        self.assertEqual(node_d.to_html(), '<p href="https://www.google.com">Im a paragraph with link</p>')
        try:
            node_e = LeafNode("p", None, {"href":"https://www.google.com"}).to_html()
            self.assertTrue(False)
        except ValueError as e:
            self.assertTrue(True)
            

    def test_parent_to_html(self):
        child_a = LeafNode(None, "Hello There!")
        child_b = LeafNode(None, "I have a link?", {"href":"https://www.google.com"})
        child_c = LeafNode("p", "Im a paragraph")
        child_d = LeafNode("p", "Im a paragraph with link", {"href":"https://www.google.com"})
        child_e = LeafNode("p", None, {"href":"https://www.google.com"})

        # testing errors
        try:
            parent_a = ParentNode(None, [child_a, child_b]).to_html()
        except ValueError as e:
            self.assertTrue("Tag not set for ParentNode" in str(e))

        try:
            parent_b = ParentNode("div", None).to_html()
        except ValueError as e:
            self.assertTrue("Children not set for ParentNode" in str(e))

        try:
            parent_c = ParentNode("div", [child_e]).to_html()
        except ValueError as e:
            self.assertTrue("Value not set for LeafNode" in str(e))

        # testing children one level
        parent_d = ParentNode("div", [child_a])
        self.assertEqual(parent_d.to_html(), "<div>Hello There!</div>")

        parent_e = ParentNode("p", [child_b, child_c])
        self.assertEqual(parent_e.to_html(), "<p>I have a link?<p>Im a paragraph</p></p>")

        # nested parents
        parent_f = ParentNode("div", [parent_e, child_d])
        self.assertEqual(parent_f.to_html(), '<div><p>I have a link?<p>Im a paragraph</p></p><p href="https://www.google.com">Im a paragraph with link</p></div>')


if __name__ == "__main__":
    unittest.main()