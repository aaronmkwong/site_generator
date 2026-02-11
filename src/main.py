import sys
from copystatic import copy_directory_recursive
from gencontent import generate_pages_recursive

def main():
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    copy_directory_recursive("static", "docs")
    generate_pages_recursive('content/', 'template.html', 'docs/', basepath)
	
# main() function only called when file directly run
if __name__ == "__main__":
      main()