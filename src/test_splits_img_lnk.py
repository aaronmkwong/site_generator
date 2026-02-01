# verify code works as expected

import unittest

from textnode  import extract_markdown_images, extract_markdown_links, split_nodes_link, split_nodes_image

class TestMarkdownExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )   
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://www.testlink.dev)"
            )   
        self.assertListEqual([("link", "https://www.testlink.dev")], matches)

if __name__ == "__main__":
	unittest.main()