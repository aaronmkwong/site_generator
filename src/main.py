import os
import shutil
import sys
from copystatic import copy_directory_recursive
from gencontent import generate_pages_recursive

def main():
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    dir_path = "docs"

    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        shutil.rmtree(dir_path) 

    copy_directory_recursive("static", "docs")
    generate_pages_recursive('content/', 'template.html', 'docs/', basepath)
	
# main() function only called when file directly run
if __name__ == "__main__":
      main()