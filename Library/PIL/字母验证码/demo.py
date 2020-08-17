import tesserocr
from PIL import Image

str = 'xxxx.jpg'
image = Image.open(str)
result = tesserocr.image_to_text(image).strip()
print(result)