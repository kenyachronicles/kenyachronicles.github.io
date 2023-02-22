source = "assets/images/prologue" 
dest = source + "/thumbnails"

from PIL import Image
import os

files = os.listdir(source)

def get_thumbnails(files): 

    if not os.path.exists(dest):
        os.makedirs(dest)

    for filename in files:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            # Load just once, then successively scale down
            im=Image.open(os.path.join(source, filename))
            im = im.convert('RGB')
            im.thumbnail((140,140))
            im.save(f"{dest}/{filename}")
     

get_thumbnails(files)