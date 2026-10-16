"""Create delivery-sized WebP variants from the saved image-generation manifest."""
import json
from pathlib import Path
from PIL import Image, ImageOps

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'reference/blog-cover-art-direction.json').read_text(encoding='utf-8'))
posts_path = root / 'content/posts.json'
posts = json.loads(posts_path.read_text(encoding='utf-8'))
destination = root / 'public/assets/blog'
destination.mkdir(parents=True, exist_ok=True)
for item in manifest['covers']:
    post = posts[item['index']]
    original = Path(item['generatedFile'])
    with Image.open(original) as image:
        image = ImageOps.fit(image.convert('RGB'), (1280, 720), method=Image.Resampling.LANCZOS)
        stem = post['slug'] + '-cover'
        for width in (1280, 960, 480):
            filename = stem + ('' if width == 1280 else f'-{width}') + '.webp'
            variant = image if width == 1280 else image.resize((width, width * 9 // 16), Image.Resampling.LANCZOS)
            variant.save(destination / filename, 'WEBP', quality=86, method=6)
        print(f"{post['slug']}: 1280, 960 and 480px WebP variants")

metadata_path = root / 'data/page-metadata.json'
metadata = json.loads(metadata_path.read_text(encoding='utf-8'))
metadata['/blog/']['image'] = '__SITE_ORIGIN__' + posts[0]['image']
metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
