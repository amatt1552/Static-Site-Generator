from textnode import TextNode, TextType
import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if(block != "\n"):
            new_blocks.append(block.strip("\n "))
    return new_blocks

def convert_markdown(old_nodes):
    new_nodes = split_nodes_image(old_nodes)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    return new_nodes

# TODO Create function that handles delimiter for you. 
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    # this is done to prevent overwritting already modified text.
    # will not allow nested text_types
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    return handle_nodes_with_links(old_nodes, TextType.IMAGE, "!")

def split_nodes_link(old_nodes):
    return handle_nodes_with_links(old_nodes)

def handle_nodes_with_links(old_nodes, text_type = TextType.LINK, delimiter = ""):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        
        original_text = old_node.text
        data = [] 
        # determines which text_type is used and handles if is incorrect
        match text_type:
            case TextType.IMAGE:
                data = extract_markdown_images(old_node.text)
            case TextType.LINK:
                data = extract_markdown_links(old_node.text)
            case _:
                raise ValueError("text_type must be IMAGE or LINK TextType.")
        # if nothing was extracted adds node to the list.
        if len(data) == 0:
            new_nodes.append(old_node)
            continue

        for item in data:
            text = item[0]
            link = item[1]
            sections = original_text.split(f"{delimiter}[{text}]({link})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            
            # requested to not add empty string TextNode to new_nodes list
            if(sections[0] != ""):
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(text, text_type, link))
            
            # removes all text appended to split_nodes from original text
            original_text = sections[1]
        # checks for extra text at the end of old_node's text  
        if(original_text != ""):
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
 
# I thought if was [alt text] without link it would only get [alt text] but was incorrect.
def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    #print("Matches:", matches, "matches end")
    #matches_count = 0
    #for match in matches:
    #    matches_count += len(match)
    
    #if(matches_count % 2 != 0):
    #    raise IndexError("Error: Alt text not matched with image link or vice versa.")

    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    
    return matches