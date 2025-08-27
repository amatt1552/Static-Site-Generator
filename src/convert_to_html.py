import re
from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import(
    convert_markdown
    )
from block_markdown import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks
)

def text_to_html_node(text_node):
        match(text_node.text_type):
            case TextType.TEXT:
                return LeafNode(None, text_node.text)
            case TextType.BOLD:
                return LeafNode("b", text_node.text)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text)
            case TextType.CODE:
                return LeafNode("code", text_node.text)
            case TextType.LINK:
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case TextType.IMAGE:
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            case _:
                raise Exception("Passed Text Type does not exist")


def markdown_to_html_nodes(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        node = __block_to_html_node(block)
        if(node.tag != "pre"):
            inline_nodes = __block_to_inline(node)
            nodes.append(inline_nodes)
        else:
            nodes.append(node)
            
    return ParentNode("div", nodes)

def __block_to_inline(old_node):
    if(not old_node.children):
        child_text_nodes = convert_markdown([TextNode(old_node.value, TextType.TEXT)])
        leaf_nodes = []
        for child in child_text_nodes:
            leaf_nodes.append(text_to_html_node(child))
        if(len(leaf_nodes) > 0):
            return ParentNode(old_node.tag, leaf_nodes, old_node.props)
        return old_node
    else:
        leaf_nodes = []
        for child in old_node.children:
            leaf_nodes.append(__block_to_inline(child))
        return ParentNode(old_node.tag, leaf_nodes, old_node.props)

def __block_to_html_node(block):
   block_type = block_to_block_type(block)
   match(block_type):
            case BlockType.HEADING:
                i = 0
                while block[i] == "#" and i < 6:
                    i += 1
                return LeafNode(f"h{i}", block[i + 1:])
       
            case BlockType.CODE:
                leaf_node = LeafNode("code", __remove_from_lines_code(block))
                return ParentNode("pre", [leaf_node])
       
            case BlockType.QUOTE:
                return LeafNode("blockquote", __remove_from_lines(block, ">"))
            
            case BlockType.UNORDERED_LIST:
                modified_block = __remove_from_lines(block, "- ")
                leaf_nodes = __add_li_to_lines(modified_block)
                return ParentNode("ul", leaf_nodes)
            
            case BlockType.ORDERED_LIST:
                modified_block = __remove_from_lines_ol(block)
                leaf_nodes = __add_li_to_lines(modified_block)
                return ParentNode("ol", leaf_nodes)
            
            case BlockType.PARAGRAPH:
                return LeafNode("p", block)
            case _:
                raise Exception("Passed Block Type does not exist")

# removes ``` from start and end of each line for code
def __remove_from_lines_code(block):
        new_block = block.strip("```")
        # I strip it again in case there are endlines or spaces at start or end.
        return new_block.strip()

# removes value from start of each line from a block
def __remove_from_lines(block, text_removed):
    split_block = block.split("\n")
    new_block = []
    for line in split_block:
        split_line = line.split(text_removed, 1)
        new_block.append(split_line[1])
    return "\n".join(new_block)

# removes number and . from start of each line for ordered list
def __remove_from_lines_ol(block):
    split_block = block.split("\n")
    new_block = []
    pattern = r"^\d+\. "
    for line in split_block:
        text_removed = re.match(pattern, line)
        split_line = line.split(text_removed[0], 1)
        new_block.append(split_line[1])
    return "\n".join(new_block)

def __add_li_to_lines(block):
    split_block = block.split("\n")
    leaf_nodes = []
    for line in split_block:
        leaf_nodes.append(LeafNode("li", line))
    return leaf_nodes
