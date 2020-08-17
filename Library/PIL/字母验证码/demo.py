import tesserocr
from PIL import Image

image_str = 'xxxx.jpg'
image = Image.open(image_str).convert('L')

threshold = 160
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
result = tesserocr.image_to_text(image)
print(result)


