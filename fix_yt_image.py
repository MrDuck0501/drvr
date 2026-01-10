
import os
import urllib.request

ASSETS_DIR = 'assets/images'
os.makedirs(ASSETS_DIR, exist_ok=True)

# New working URL for YT card
new_url = "https://images.unsplash.com/photo-1622979135225-d2ba269fb1bd?auto=format&fit=crop&q=80&w=800"
filename = "yt_cover.jpg"
old_broken_url = "https://images.unsplash.com/photo-1626544827763-d516dce335a2?auto=format&fit=crop&q=80&w=800"

print(f"Downloading {new_url}...")
try:
    req = urllib.request.Request(new_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        with open(os.path.join(ASSETS_DIR, filename), 'wb') as f:
            f.write(response.read())
        print(f"Saved {filename}")

    # Update index.html
    index_path = 'index.html'
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the broken URL with local path
    if old_broken_url in content:
        content = content.replace(old_broken_url, f"assets/images/{filename}")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated index.html")
    else:
        print("Could not find old URL to replace (maybe already replaced?)")

except Exception as e:
    print(f"Error: {e}")
