import sys
import os
from PIL import Image
path = sys.argv[1]
new=sys.argv[2]
if not os.path.exists(new):
   os.makedirs(new)

for filename in os.listdir(path):
   img=Image.open(f"{path}{filename}")
   clean=os.path.splitext(filename)[0]
   img.save(f"{new}{clean}.png",'png')

