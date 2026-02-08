import os
import shutil

def copy_directory_recursive(src, dst, is_root_call=True):
    """
    Recursively copy contents of src directory into dst directory.
    
    On the root call:
      1. Deletes dst if it exists
      2. Recreates dst
    
    During recursion:
      - Copies files
      - Creates subdirectories as needed
      - Logs each file copied
    """

    # Root call setup: clean destination directory
    if is_root_call:
        if os.path.exists(dst):
            shutil.rmtree(dst)
            print(f"Deleted existing directory: {dst}")

        os.mkdir(dst)
        print(f"Created directory: {dst}")

    # Iterate through source directory contents
    for entry in os.listdir(src):
        src_path = os.path.join(src, entry)
        dst_path = os.path.join(dst, entry)

        # If it's a file, copy it
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {src_path} -> {dst_path}")

        # If it's a directory, create it and recurse
        else:
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
                print(f"Created directory: {dst_path}")

            copy_directory_recursive(src_path, dst_path, is_root_call=False)