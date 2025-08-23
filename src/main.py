from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter, 
    split_nodes_image, 
    convert_markdown,) 
from block_markdown import (
    markdown_to_blocks
)
from convert_to_html import(
    markdown_to_html_nodes
)

def main():
    #text_node = TextNode("heheheha!", TextType.LINK, "https://supercell.com/en/games/clashroyale/")
    #print(text_node)
    
    md = """
1. Im ordered
2. me too!
3. me three!

1. I'm a lonely list

100. I'm huge!

1. still a list! 2. not a list
"""
    html_nodes = markdown_to_html_nodes(md)
    print(html_nodes.to_html())


if __name__ == "__main__":
    main()