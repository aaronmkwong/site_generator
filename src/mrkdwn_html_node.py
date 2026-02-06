from htmlnode import *
from textnode import *

# High-level pipeline:
# 1. Split the markdown document into block strings.
# 2. Convert each block into a block-level HTMLNode based on its type.
#    a. Detect the block type (heading, paragraph, list, etc.).
#    b. Build the correct HTML structure for that block.
#    c. For non-code blocks, parse inline markdown with text_to_children().
#    d. For code blocks, skip inline parsing and keep text as-is.
# 3. Wrap all block nodes in a single parent <div> and return it.

# main function
def markdown_to_html_node(markdown):

    # Step 1: split the raw markdown into logical blocks
    blocks = markdown_to_blocks(markdown)

    block_nodes = []

    # Step 2: convert each block to the appropriate HTMLNode
    for block in blocks:

        # Determine type and build the matching HTMLNode for this block
        node = block_to_html_node(block)
        block_nodes.append(node)

    # Step 3: make all block nodes children of a single root <div>
    return ParentNode("div", block_nodes)

# Given a single markdown block string, return the corresponding block-level HTMLNode        
def block_to_html_node(block):

    # Determine the type of this block (heading, paragraph, list, etc.)
    block_type = block_to_block_type(block)

     # Dispatch to the right handler based on the detected block type
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)

    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)

    if block_type == BlockType.CODE:
        return code_to_html_node(block)

    if block_type == BlockType.QUOTE:
        return blockquote_to_html_node(block)

    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)

    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)

    raise ValueError("Unknown block type")

def heading_to_html_node(block):

    # Count leading '#' characters to determine heading level
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break

    # Extract the heading text after the '#' characters
    text = block[level:].strip()

    # Parse inline markdown inside the heading text into child HTMLNodes
    children = text_to_children(text)

    # Wrap children in the appropriate <h1>–<h6> tag
    return ParentNode(f"h{level}", children)

def paragraph_to_html_node(block):

    # Paragraphs may span multiple lines; join lines into a single space-separated string
    text = " ".join(block.split("\n"))

    # Parse inline markdown inside the paragraph into child HTMLNodes
    children = text_to_children(text)

    # Wrap children in a <p> element
    return ParentNode("p", children)

def code_to_html_node(block):

    # Code blocks are special: they should not parse inline markdown
    lines = block.split("\n")

    # Strip the opening and closing ``` lines and keep the inner text as-is
    code_text = "\n".join(lines[1:-1])

    # Treat the entire code block content as plain text
    text_node = TextNode(code_text, TextType.TEXT)

    # Convert the TextNode to an HTMLNode (typically a <text> or similar node)
    code_child = text_node_to_html_node(text_node)

    # Construct the nested <pre><code>...</code></pre> structure
    code_node = ParentNode("code", [code_child])
    return ParentNode("pre", [code_node])

def blockquote_to_html_node(block):

    # Strip leading '>' markers from each line and clean whitespace
    lines = block.split("\n")

    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line.lstrip(">").strip())

    # Join quote lines into a single text string
    text = " ".join(cleaned_lines)

    # Parse inline markdown inside the quote
    children = text_to_children(text)

    # Wrap children in a <blockquote> element
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):

    # Split the block into individual list item lines
    lines = block.split("\n")

    list_items = []

    for line in lines:
        # Remove the leading "- " marker from each line
        text = line[2:].strip()

        # Parse inline markdown for each list item
        children = text_to_children(text)

        # Wrap children in an <li> element
        list_items.append(ParentNode("li", children))

     # Wrap all items in a <ul> element
    return ParentNode("ul", list_items)

def ordered_list_to_html_node(block):

    # Split the block into individual list item lines
    lines = block.split("\n")

    list_items = []

    for line in lines:
        # Remove the leading "1. ", "2. ", etc. and keep the item text
        parts = line.split(".", 1)
        text = parts[1].strip()

        # Parse inline markdown for each list item
        children = text_to_children(text)

        # Wrap children in an <li> element
        list_items.append(ParentNode("li", children))

     # Wrap all items in an <ol> element
    return ParentNode("ol", list_items)

# Convert an inline markdown string into a list of child HTMLNodes
def text_to_children(text):
     # 1. Convert raw text into TextNodes (plain, bold, italic, code, links, images, etc.)
    text_nodes = text_to_textnodes(text)
    
    # 2. Convert each TextNode into the corresponding HTMLNode
    children = []
    for tn in text_nodes:
        children.append(text_node_to_html_node(tn))
    
    # 3. Return the list of HTMLNodes to be used as children in a parent node
    return children
