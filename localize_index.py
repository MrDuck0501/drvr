
import os
import re
import hashlib
import urllib.request

ASSETS_DIR = 'assets/images'
os.makedirs(ASSETS_DIR, exist_ok=True)

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all http/https image URLs that are inside quotes
# Simple regex to catch the image: "https://..."
matches = re.findall(r'image:\s*"(https?://[^"]+)"', content)
matches += re.findall(r'src="(https?://[^"]+)"', content)

new_content = content

for url in set(matches):
    try:
        # Generate filename
        ext = '.jpg'
        if '.png' in url.lower(): ext = '.png'
        if '.webp' in url.lower(): ext = '.webp'
        
        filename = hashlib.md5(url.encode()).hexdigest() + ext
        local_path = f"{ASSETS_DIR}/{filename}"
        
        # Download
        if not os.path.exists(local_path):
            print(f"Downloading {url}...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                with open(local_path, 'wb') as f:
                    f.write(response.read())
        
        # Replace in content (handle simple relative path replacement)
        # Use forward slashes for web stats
        replacement_path = f"assets/images/{filename}"
        new_content = new_content.replace(url, replacement_path)
        print(f"Localized {url} -> {replacement_path}")
        
    except Exception as e:
        print(f"Failed to process {url}: {e}")

if new_content != content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated index.html")
else:
    print("No changes needed")
