from enum import Enum
from htmlnode import LeafNode

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
		


			

			




		
 

