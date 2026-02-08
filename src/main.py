from copystatic import copy_directory_recursive

# previous project lines retained but commented out in case needed
#from  textnode import TextType, TextNode

def Main():
	copy_directory_recursive("static", "public")
	
	# previous project lines retained but commented out in case needed
      
	# node = TextNode("this is some anchor text", TextType.LINK, "https://www.boot.dev")
	# print(node)

# main() function only called when file directly run
if __name__ == "__main__":
    Main()

    copy_directory_recursive("static", "public")
   