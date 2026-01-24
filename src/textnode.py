from enum import Enum

# types of inline text
# since parsing markdown text to HTML text we need an intermediate representation

class TextType(Enum):
        PLAIN  = "text"
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



