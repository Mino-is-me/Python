import os
from PIL import Image

target_drive = 'E:/wip/'

for root, dirs, files in os.walk(target_drive):
    for filename in files:
        print(filename)
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.tga') or filename.lower().endswith('.jpeg'):
            image_path = os.path.join(root, filename)
            image = Image.open(image_path)
            width, height = image.size
            if width > 2048 or height > 2048:
                new_width = 2048
                new_height = int(height * new_width / width)
                resized_image = image.resize((new_width, new_height))
                resized_image.save(image_path)
print("All images resized successfully.")