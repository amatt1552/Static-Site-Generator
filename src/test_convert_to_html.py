import unittest
from block_markdown import (
    markdown_to_blocks, 
    block_to_block_type, 
    BlockType
)
from convert_to_html import markdown_to_html_nodes

class TestInlineMarkdown(unittest.TestCase):
    def test_markdown_to_html_heading(self):
        md = """
# HEADING

### HEADING 3

###### HEADING 6
"""
        html_nodes = markdown_to_html_nodes(md)
        self.assertEqual(
            html_nodes.to_html(), 
            "<div>"+
            "<h1>HEADING</h1>" +
            "<h3>HEADING 3</h3>" +
            "<h6>HEADING 6</h6>" +
            "</div>"
        )
        
    def test_markdown_to_html_code(self):
        md = """
```code block```

```
big
code block
```
"""

        html_nodes = markdown_to_html_nodes(md)
        self.assertEqual(
            html_nodes.to_html(), 
            
                "<div>" +
                "<pre>" +
                "<code>code block</code>" +
                "</pre>" +
                "<pre>" +
                "<code>big\ncode block</code>" +
                "</pre>" +
                "</div>"
            
        )

    def test_markdown_to_html_quote(self):
        md = """
>I'm a quote
>me too!
>no! I am

>I'm a lonely quote

>>Still a quote!
"""
        html_nodes = markdown_to_html_nodes(md)
        self.assertEqual(
            html_nodes.to_html(), 
            
                "<div>" +
                "<blockquote>" +
                "I'm a quote\nme too!\nno! I am" +
                "</blockquote>" +
                "<blockquote>" +
                "I'm a lonely quote" +
                "</blockquote>" +
                "<blockquote>" +
                ">Still a quote!" +
                "</blockquote>" +
                "</div>"
            
        )
    
    def test_markdown_to_html_unordered(self):
        md = """
- Im unordered
- me too!
- no! I am

- I'm a lonely list
"""
        html_nodes = markdown_to_html_nodes(md)
        self.assertEqual(
            html_nodes.to_html(), 
            
                "<div>" +
                "<ul>" +
                "<li>Im unordered</li>" +
                "<li>me too!</li>" +
                "<li>no! I am</li>" +
                "</ul>" +
                "<ul>" +
                "<li>I'm a lonely list</li>" +
                "</ul>" +
                "</div>"
            
        )

    def test_markdown_to_html_ordered(self):
        md = """
1. Im ordered
2. me too!
3. me three!

1. I'm a lonely list

100. I'm huge!

1. still a list! 2. not a list
"""
        html_nodes = markdown_to_html_nodes(md)
        self.assertEqual(
            html_nodes.to_html(),
                "<div>" +
                "<ol>" +
                "<li>Im ordered</li>" +
                "<li>me too!</li>" +
                "<li>me three!</li>" +
                "</ol>" +
                "<ol>" +
                "<li>I'm a lonely list</li>" +
                "</ol>" +
                "<ol>" +
                "<li>I'm huge!</li>" +
                "</ol>" +
                "<ol>" +
                "<li>still a list! 2. not a list</li>" +
                "</ol>" +
                "</div>"
            
        )

    def test_markdown_to_html_paragraph(self):
        md = """
I'm talking
No I'm talking
No me!

I'm a lonely paragraph

"""
        html_nodes = markdown_to_html_nodes(md)
        self.assertEqual(
            html_nodes.to_html(),
                "<div>" +
                "<p>" +
                "I'm talking\nNo I'm talking\nNo me!"
                "</p>"+
                "<p>" +
                "I'm a lonely paragraph"
                "</p>"+
                "</div>"
            
        )
    
if __name__ == "__main__":
    unittest.main()