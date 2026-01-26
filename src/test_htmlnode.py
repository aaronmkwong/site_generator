# verify code works as expected

import unittest

from htmlnode  import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
	
	# test is an empty string
	def test_no_props(self):
		node = HTMLNode(props=None)
		self.assertEqual('', node.props_to_html())

	# test has leading space and "key=value" pattern
	def test_single_props(self):
		node = HTMLNode(props={"href": "https://www.test.com"})
		self.assertEqual(' href="https://www.test.com"', node.props_to_html())

	# test has leading space, attributes have single space separation
	# has "key=value" pattern without order dependence   
	def test_many_props(self):
		node = HTMLNode(props={"href1": "https://www.test1.com", "href2": "https://www.test2.com"})
		html = node.props_to_html()
		self.assertTrue(html.startswith(" "))
		self.assertIn('href1="https://www.test1.com"', html)
		self.assertIn('href2="https://www.test2.com"', html)

class TestLeafNode(unittest.TestCase):

	# test html rendered correctly with p tag
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	# test html rendered no tag
	def test_leaf_to_html_no_tag(self):
		node = LeafNode(None, "Hello, world!")
		self.assertEqual(node.to_html(), "Hello, world!")

	# test html rendered with props
	def test_leaf_to_html_with_props(self):
		node = LeafNode("p", "Hello, world!", {"href": "https://www.test.com"})
		self.assertEqual(node.to_html(), '<p href="https://www.test.com">Hello, world!</p>')

class TestParentNode(unittest.TestCase):

	# test has children
	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	# test has grandchildren
	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
        	parent_node.to_html(),
        	"<div><span><b>grandchild</b></span></div>",
    	)

if __name__ == "__main__":
	unittest.main()
