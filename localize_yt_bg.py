
import os
import urllib.request
import hashlib

ASSETS_DIR = 'assets/images'
os.makedirs(ASSETS_DIR, exist_ok=True)

url = "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?q=80&w=1000&auto=format&fit=crop"
local_filename = hashlib.md5(url.encode()).hexdigest() + ".jpg"
local_path = os.path.join(ASSETS_DIR, local_filename)

print(f"Downloading {url}...")
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        with open(local_path, 'wb') as f:
            f.write(response.read())
    print(f"Saved {local_filename}")
    
    # Update index.html
    index_path = 'index.html'
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if url in content:
        content = content.replace(url, f"assets/images/{local_filename}")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated index.html")
    else:
        print("URL not found in index.html (maybe already replaced?)")

except Exception as e:
    print(f"Error: {e}")
