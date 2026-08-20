import os
import sys
import re
import io
import requests
from PIL import Image

UPLOAD_URL = "https://pic.186021.xyz/upload"
DOMAIN = "https://pic.186021.xyz"
MAX_WIDTH = 1000  # 最大宽度限制为 1000 像素
QUALITY = 85      # JPEG 压缩质量

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def resize_and_compress(img_bytes, ext):
    if ext.lower() in ['gif', 'svg']:
        return img_bytes, 0
    try:
        img = Image.open(io.BytesIO(img_bytes))
        width, height = img.size
        changed = False
        
        # 只要宽度大于最大宽度限制，就进行等比缩放
        if width > MAX_WIDTH:
            new_height = int(height * (MAX_WIDTH / width))
            img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
            changed = True
            width = MAX_WIDTH
            
        if changed or ext.lower() in ['jpg', 'jpeg', 'png']:
            out_io = io.BytesIO()
            save_format = img.format if img.format else ('JPEG' if ext.lower() in ['jpg', 'jpeg'] else ext.upper())
            if save_format == 'MPO': save_format = 'JPEG'
            
            if save_format in ['JPEG', 'JPG']:
                img.save(out_io, format='JPEG', quality=QUALITY, optimize=True)
            elif save_format == 'PNG':
                img.save(out_io, format='PNG', optimize=True)
            else:
                img.save(out_io, format=save_format)
            return out_io.getvalue(), width
        return img_bytes, width
    except Exception as e:
        print(f"  [Resize/Compress Error] {e}")
    return img_bytes, 0

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
                
                # 自动缩放和压缩图片，并返回图片最终宽度
                img_bytes, final_width = resize_and_compress(img_bytes, ext)
                
                files = {'file': (f'image.{ext}', img_bytes, f'image/{ext}')}
                up_resp = requests.post(UPLOAD_URL, files=files, headers=headers, timeout=15)
                
                if up_resp.status_code == 200:
                    res_json = up_resp.json()
                    if isinstance(res_json, list) and len(res_json) > 0 and 'src' in res_json[0]:
                        new_url = f"{DOMAIN}{res_json[0]['src']}"
                        url_map[url] = (new_url, final_width)
                        print(f"  -> Uploaded (Resized/Compressed): {new_url} (width: {final_width}px)")
        except Exception as e:
            print(f"  -> Failed {url}: {e}")

    for old_u, (new_u, w) in url_map.items():
        if w > 400:
            # 对于大截图，自动重构为 100% 宽度并居中的 HTML 标签以等宽于正文
            pattern = rf'!\[(.*?)\]\({re.escape(old_u)}\)'
            content = re.sub(pattern, rf'<img src="{new_u}" alt="\1" style="width: 100%; display: block; margin: 0 auto;" />', content)
        # 兜底直接替换
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