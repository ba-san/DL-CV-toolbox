#https://note.nkmk.me/python-pillow-image-resize/

import os
import glob
from PIL import Image

files = glob.glob('./shibuya-128-new/*/*/*.jpg')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((int(32), int(32)))
    ftitle, fext = os.path.splitext(f)
    if not os.path.exists("./resized" + os.path.dirname(ftitle[1:])):
        os.makedirs("./resized" + os.path.dirname(ftitle[1:]))
    img_resize.save("./resized" + ftitle[1:] + '_resized' + fext)
