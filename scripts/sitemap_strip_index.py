import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sitemap = Path(sys.argv[1])

# Parse XML
tree = ET.parse(sitemap)
root = tree.getroot()

# Iterate over every <loc> tag in the sitemap (with correct namespace)
for loc in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
    # Extract the text (URL) inside the <loc> tag
    url = loc.text

    if url and url.endswith("index.html"):
        # Remove 'index.html' from the URL (last 10 characters)
        new_url = url[:-10]

        # Ensure the modified URL ends with a trailing slash
        if not new_url.endswith("/"):
            new_url += "/"

        # Update the <loc> tag's text with the new URL
        loc.text = new_url

# Register the sitemap XML namespace so it appears in the output
ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")

# Write the modified XML tree back to the original file, with declaration and
# UTF-8 encoding
tree.write(sitemap, encoding="utf-8", xml_declaration=True)
