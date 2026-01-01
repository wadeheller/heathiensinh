import os
import json

image_folder = 'Image'
extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.webm', '.webp']

files = []
if os.path.exists(image_folder):
    for file in sorted(os.listdir(image_folder)):
        if any(file.lower().endswith(ext) for ext in extensions):
            files.append(f'Image/{file}')

# Tạo file JSON
with open('images.json', 'w', encoding='utf-8') as f:
    json.dump({'images': files}, f, indent=2, ensure_ascii=False)

print(f'✅ Đã tạo images.json với {len(files)} files:')
for i, file in enumerate(files, 1):
    print(f'  {i}. {file}')
