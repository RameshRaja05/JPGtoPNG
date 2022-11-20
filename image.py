
from PIL import Image, ImageFilter

img = Image.open('./images/astro.jpg')
img.thumbnail((450,420))
print(img.size) #it automatically fix the height and width for image it is intellisense.