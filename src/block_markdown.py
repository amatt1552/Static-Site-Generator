import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unorderd list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        # only adds blocks that arent empty or endlines
        if(block != "\n" and block != ""):
            new_blocks.append(block.strip("\n "))
    return new_blocks

def block_to_block_type(block):
    # test for heading (1-6 # )
    max_length = 7
    if(block[0] == "#"):
        for i in range(max_length - 1):
            try:
                if(block[i] == "#" and block[i + 1] == " "):
                    return BlockType.HEADING
            except IndexError:
                break
    
    # test for code block (start and end ```)
    if(block.startswith("```") and block.endswith("```")):
        return BlockType.CODE
    
    # test for quote (each line >)
    split_block = block.split("\n")
    quote_valid = True
    for line in split_block:
        if(not line.startswith(">")):
            quote_valid = False
            break
    if(quote_valid):
        return BlockType.QUOTE
        
    # test for unorderedlist (each line - )
    unordered_list_valid = True
    for line in split_block:
        if(not line.startswith("- ")):
            unordered_list_valid = False
            break
    if(unordered_list_valid):
        return BlockType.UNORDERED_LIST
        
    # test for orderedlist (each line #. )
    ordered_list_valid = True
    for line in split_block:
        pattern = r"^\d+\. "
        if(not re.match(pattern, line)):
            ordered_list_valid = False
            break
        
        # I didnt like the amount of ifs and fors here!
        # leaving this here as a reminder of why regex is useful.
        
        #if(line[0].isdigit()):
        #   for i in range(len(line) -1):
        #       if(not line[i].isdigit()):
        #           if(line[i:i+1] == ". ")
        #               break
        #           ordered_list_valid = False
        #           break
    if(ordered_list_valid):
        return BlockType.ORDERED_LIST
        
    # paragraph when all test fail
    return BlockType.PARAGRAPH
