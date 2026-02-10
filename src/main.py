from copystatic import copy_directory_recursive
from gencontent import generate_page

def main():
    copy_directory_recursive("static", "public")
    generate_page('content/index.md', 'template.html', 'public/index.html')
	
# main() function only called when file directly run
if __name__ == "__main__":
      main()