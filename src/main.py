from textnode import TextNode, TextType
from markdown_conversion import split_nodes_delimiter, split_nodes_image, convert_markdown, markdown_to_blocks

def main():
    #text_node = TextNode("heheheha!", TextType.LINK, "https://supercell.com/en/games/clashroyale/")
    #print(text_node)
    
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    for node in blocks:
        print(node)


if __name__ == "__main__":
    main()