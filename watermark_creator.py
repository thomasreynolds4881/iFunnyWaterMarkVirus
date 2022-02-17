from PIL import Image
import os
import urllib.request

# Grab watermark
urllib.request.urlretrieve('https://www.dropbox.com/s/yiukpingxe55pqi/watermark.jpg?dl=1', 'wm.png')
wm = Image.open('wm.png')
wm_w, wm_h = wm.size

# Grab each image
valid_exts = ['.jpeg', '.jpg', '.png']

for filename in os.listdir("."):
    f = os.path.join(filename)
    # checking if it is an image
    if os.path.isfile(f) and os.path.splitext(f)[1] in valid_exts:
        p = Image.open(f)
        p_w, p_h = p.size
        offset = ((p_w - wm_w), (p_h - wm_h))
        p.paste(wm, offset)
        p.save(os.path.basename(f))

# Remove wm image from dir
os.remove('wm.png')