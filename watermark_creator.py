from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Grab watermark
wm = Image.open("watermark.jpg")
wm_w, wm_h = wm.size

# Grab picture
p = Image.open("images/image2.jpg")
p_w, p_h = p.size
#print(w,h)
offset = ((p_w - wm_w), (p_h - wm_h))
p.paste(wm, offset)
p.save('out.png')