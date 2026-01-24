# verify code works as expected

import unittest

from htmlnode  import HTMLNode

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
		
if __name__ == "__main__":
	unittest.main()
