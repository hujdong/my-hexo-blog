import os
import sys
import re
import requests

UPLOAD_URL = "https://pic.186021.xyz/upload"
DOMAIN = "https://pic.186021.xyz"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def migrate_file(post_path):
    if not os.path.exists(post_path):
        return
    with open(post_path, "r", encoding="utf-8") as f:
        content = f.read()

    vocus_urls = re.findall(r'https?://images\.vocus\.cc/[^\s\)\"]+', content)
    ext_urls = re.findall(r'https?://(?!pic\.186021\.xyz)[^\s\)\"]+\.(?:jpg|png|jpeg|webp|gif)', content, re.IGNORECASE)
    all_urls = set(vocus_urls + ext_urls)

    if not all_urls:
        return

    print(f"[Auto Migrate] Processing {os.path.basename(post_path)} ({len(all_urls)} images)...")
    url_map = {}

    for url in all_urls:
        try:
            resp = requests.get(url, headers=headers, timeout=15)
            if resp.status_code == 200:
                img_bytes = resp.content
                ext = 'jpg'
                if '.png' in url.lower(): ext = 'png'
                elif '.webp' in url.lower(): ext = 'webp'
                elif '.gif' in url.lower(): ext = 'gif'
                
                files = {'file': (f'image.{ext}', img_bytes, f'image/{ext}')}
                up_resp = requests.post(UPLOAD_URL, files=files, headers=headers, timeout=15)
                
                if up_resp.status_code == 200:
                    res_json = up_resp.json()
                    if isinstance(res_json, list) and len(res_json) > 0 and 'src' in res_json[0]:
                        new_url = f"{DOMAIN}{res_json[0]['src']}"
                        url_map[url] = new_url
                        print(f"  -> Uploaded: {new_url}")
        except Exception as e:
            print(f"  -> Failed {url}: {e}")

    for old_u, new_u in url_map.items():
        content = content.replace(old_u, new_u)

    with open(post_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    posts_dir = r"D:\hexo-new-blog\source\_posts"
    if len(sys.argv) > 1:
        migrate_file(sys.argv[1])
    else:
        for f in os.listdir(posts_dir):
            if f.endswith(".md"):
                migrate_file(os.path.join(posts_dir, f))