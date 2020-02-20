import cv2
import numpy as np
import glob
from matplotlib import pylab as plt

files = glob.glob('./crowd_night_annotation/*.jpg')

for filename in files:
    
    img = cv2.imread(filename)
    f, ax_list = plt.subplots(2, 1, figsize=(10, 5))
    color = ('b','g','r')
    
    # before
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        ax = ax_list[0]
        ax.plot(histr,color = col)
        plt.xlim([0,256])
    
    # equalization
    for j in range(3):
        img[:, :, j] = cv2.equalizeHist(img[:, :, j])  # equalize for each channel
        
    # clahe
    # clipLimit=2.0
    # tileGrid = 8
    # img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    # clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=(tileGrid,tileGrid))
    # img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
    # img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        
    # after
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        ax = ax_list[1]
        ax.plot(histr,color = col)
        plt.xlim([0,256])
    
    plt.savefig(filename + "_histgram.png")
    plt.close()
    splited = filename.split('.')
    
    cv2.imwrite('.' + splited[1] + '_hist.png', cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # for general equilization
    #cv2.imwrite('.' + splited[1] + '_clahe_{}_{}.png'.format(clipLimit, tileGrid), img) # for CLAHE
