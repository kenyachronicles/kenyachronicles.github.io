source = "assets/images/prologue" 
dest_small = source + "/small"
dest_medium = source + "/medium"

from PIL import Image
import os

files:list[str] = os.listdir(source)

def get_thumbnails(files): 

    for dest in [dest_small, dest_medium]:
        if not os.path.exists(dest):
            os.makedirs(dest)

    for filename in files:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            # Load just once, then successively scale down
            im=Image.open(os.path.join(source, filename))
            im = im.convert('RGB')
            im.thumbnail((640,640))
            im.save(f"{dest_medium}/{filename}")
            im.thumbnail((140,140))
            im.save(f"{dest_small}/{filename}")
     

get_thumbnails(files)