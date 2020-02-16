#https://note.nkmk.me/python-pillow-image-resize/

import os
import glob
import pandas as pd
from PIL import Image

#https://note.nkmk.me/python-pillow-image-crop-trimming/

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

dirname = "flickr_night" # set the directory name
resized = 1024 # set the size here

files = glob.glob('./' + dirname + '/*.jpg')



for f in files:
    img = Image.open(f)
    x_ratio = float(resized)/float(img.size[0])
    img_resize = img.resize((resized, int(x_ratio*img.size[1])), Image.LANCZOS)
    img_crop = crop_center(img_resize, 1024, 768)
    ftitle, fext = os.path.splitext(f)
    flist = ftitle.split("/")
    new_folder = "./" + dirname + "_resized/"
       
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    img_crop.save(new_folder + flist[2] + '_resized.jpg')
