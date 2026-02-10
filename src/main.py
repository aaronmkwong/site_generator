from copystatic import copy_directory_recursive
from gencontent import generate_pages_recursive

def main():
    copy_directory_recursive("static", "public")
    generate_pages_recursive('content/', 'template.html', 'public/')
	
# main() function only called when file directly run
if __name__ == "__main__":
      main()