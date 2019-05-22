#https://note.nkmk.me/python-pillow-image-resize/

import os
import glob
from PIL import Image

files = glob.glob('./something_output_128_128_30_30_0/*/*/*.jpg')

resized_x = 32
resized_y = 32

for f in files:
    img = Image.open(f)
    img_resize = img.resize((resized_x, resized_y))
    ftitle, fext = os.path.splitext(f)
    flist = ftitle.split("/")
    new_folder = "../resized/" + flist[1] + "_resized_" + str(resized_x) + "_" + str(resized_y) + "/" + flist[2] + "/" + flist[3] + "/"
    
    
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    img_resize.save(new_folder + flist[4] + '_resized' + fext)
