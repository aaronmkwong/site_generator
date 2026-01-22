from  textnode import TextType, TextNode

def Main():
	node = TextNode("this is some anchor text", TextType.LINK, "https://www.boot.dev")
	print(node)

# main() function only called when file directly run
if __name__ == "__main__":
    Main()
