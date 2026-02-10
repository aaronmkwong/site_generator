import os
from mrkdwn_html_node import markdown_to_html_node


# pull h1 header from mardown file 
def extract_title(markdown):
	mrkdwn_lines = markdown.splitlines()
	for line in mrkdwn_lines:
		if len(line) > 2 and line[0] == '#' and ( line[1] == ' ' or line[1] != '#'):
			return line[1:].strip()
	raise Exception('no h1 header')
	
# create HMTL page
def generate_page(from_path, template_path, dest_path):
    # Print status message
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown file and file automatically closes here, even if an error occurs
    with open(from_path, "r", encoding="utf-8") as from_file:
        markdown_content = from_file.read()
		
    # Read template file
    with open(template_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # Convert markdown to HTML string
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract title
    title = extract_title(markdown_content)

    # Replace placeholders in template
    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    # Ensure destination directory exists
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "" and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Write final HTML to destination file
    with open(dest_path, "w", encoding="utf-8") as dest_file:
       dest_file.write(full_html)

# create HMTL pages recursively
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
 
    # Ensure destination directory exists
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    # Crawl every entry in the content directory
    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        # If entry is a directory, recurse
        if os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dest_path)

        # If entry is a markdown file, generate HTML
        elif entry.endswith(".md"):
            # Change .md to .html in destination
            dest_file_path = dest_path.replace(".md", ".html")

            generate_page(src_path, template_path, dest_file_path)
