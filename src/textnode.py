from enum import Enum
from htmlnode import LeafNode
import re

# types of inline text
# since parsing markdown text to HTML text we need an intermediate representation

class TextType(Enum):
        TEXT  = "text"
        BOLD = "bold"
        ITALIC = "italic"
        CODE = "code"
        LINK = "link"
        IMAGE = "image"

# represents various types of inline text in HTML and markdown
class TextNode:
	# initialize  arguments
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	# unit tests will rely on this method to compare objects
	def __eq__(self, other):
		if not isinstance(other,TextNode):
			return NotImplemented
		return self.text == other.text and self.text_type == other.text_type and self.url == other.url

	# prints an TextNode object for debugging to see its text, text type, url
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

# handle each type of the TextType enum and return new LeafNode object
def text_node_to_html_node(text_node):

	# return a LeafNode with no tag, just a raw text value
	if text_node.text_type == TextType.TEXT:
		return LeafNode(None, text_node.text)

	# return a LeafNode with a "b" tag and the text
	elif text_node.text_type == TextType.BOLD:
		return LeafNode('b', text_node.text)
	
	# return LeafNode with "i" tag, text
	elif text_node.text_type == TextType.ITALIC:
		return LeafNode('i', text_node.text)
	
	# return LeafNode with "code" tag, text
	elif text_node.text_type == TextType.CODE:
		return LeafNode('code', text_node.text)

	# "a" tag, anchor text, and "href" prop
	elif text_node.text_type == TextType.LINK:
		return LeafNode('a', text_node.text, {'href':text_node.url})
	
	# "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
	elif text_node.text_type == TextType.IMAGE:
		return LeafNode('img', '', {'src':text_node.url, 'alt':text_node.text})

	else:
		raise Exception()

# create TextNodes from raw markdown strings
def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	text_old_node = ''

	for old_node in old_nodes:
		text_old_node = old_node.text
		count = text_old_node.count(delimiter)
		
		# only attempt to split "text" type objects (not bold, italic, etc)
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		
		# ensure only valid markdown syntax
		if count == 0:
			new_nodes.append(old_node)
			continue 
		
		elif count % 2 != 0:
			raise Exception('invalid markdown')
		
		split_text = old_node.text.split(delimiter)
		for i, text in enumerate(split_text):
			if text == "":
				continue
			elif ( i % 2)  != 0:
				new_nodes.append(TextNode(text,text_type))
			else:
				new_nodes.append(TextNode(text,TextType.TEXT))
	
	return new_nodes 

# takes raw markdown text and return images as list of tuples
def extract_markdown_images(text):
	return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

# takes raw markdown text and return anchor text and urls as list of tuples
def extract_markdown_links(text):
	return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

# split raw markdown text into TextNodes based on images
def split_nodes_image(old_nodes):
	new_nodes = []

	# loop over each existing TextNode and split any TEXT nodes by images
	for old_node in old_nodes:
		
		# if this node is not plain TEXT, just keep it as-is
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		
		# repeatedly find the next image in the remaining text and split around it
		text_remaining = old_node.text 
		for string in extract_markdown_images(text_remaining):
			alt_text = string[0]
			img_text = string[1]
			
			before, after = text_remaining.split(f'![{alt_text}]({img_text})', maxsplit=1)
			
			# only create a TEXT node if there is non-empty text before the image
			if before != '':
				new_nodes.append(TextNode(before, TextType.TEXT))
			
			# create a IMAGE node for the current markdown image
			new_nodes.append(TextNode(alt_text, TextType.IMAGE, img_text))

			text_remaining = after

		# after processing all images, if there is leftover text, keep it as TEXT
		if text_remaining != "":
			new_nodes.append(TextNode(text_remaining, TextType.TEXT))

	return new_nodes
	
# split raw markdown text into TextNodes based on links
def split_nodes_link(old_nodes):
	new_nodes = []

	# loop over each existing TextNode and split any TEXT nodes by links
	for old_node in old_nodes:
		
		# if this node is not plain TEXT, just keep it as-is
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		
		# repeatedly find the next link in the remaining text and split around it
		text_remaining = old_node.text 
		for string in extract_markdown_links(text_remaining):
			alt_text = string[0]
			lnk_text = string[1]
			
			before, after = text_remaining.split(f'[{alt_text}]({lnk_text})', maxsplit=1)
			
			# only create a TEXT node if there is non-empty text before the link
			if before != '':
				new_nodes.append(TextNode(before, TextType.TEXT))
			
			# create a LINK node for the current markdown link
			new_nodes.append(TextNode(alt_text, TextType.LINK, lnk_text))

			text_remaining = after

		# after processing all links, if there is leftover text, keep it as TEXT
		if text_remaining != "":
			new_nodes.append(TextNode(text_remaining, TextType.TEXT))

	return new_nodes
	
# use "splitting" functions together to convert a raw string 
# of markdown-flavored text into a list of TextNode objects
def text_to_textnodes(text):
	bold_node = split_nodes_delimiter([TextNode(text)], '**', TextType.BOLD)
	ital_node = split_nodes_delimiter(bold_node, '*', TextType.ITALIC) 
	code_node = split_nodes_delimiter(ital_node, "`", TextType.CODE) 
	img_node = split_nodes_image(code_node)
	lnk_node = split_nodes_link(img_node)

	return lnk_node
		


			

			




		
 

