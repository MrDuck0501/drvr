
import os
import urllib.request
import hashlib

ASSETS_DIR = 'assets/images'
os.makedirs(ASSETS_DIR, exist_ok=True)

images = {
    "https://images.unsplash.com/photo-1626544827763-d516dce335a2?auto=format&fit=crop&q=80&w=800": "yt_cover.jpg",
    "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&q=80&w=800": "promo_cover.jpg"
}

index_path = 'index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

for url, filename in images.items():
    print(f"Downloading {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(os.path.join(ASSETS_DIR, filename), 'wb') as f:
                f.write(response.read())
            print(f"Saved {filename}")
            
            # Replace in content
            content = content.replace(url, f"assets/images/{filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
