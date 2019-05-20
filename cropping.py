import os
import cv2
import glob
import csv
import argparse
import pandas as pd
from tqdm import tqdm
import linecache, shutil

parser = argparse.ArgumentParser(description='cropping by class')
parser.add_argument('-cn', '--change_name', help='change "OO_checked" to "OO_cropped" (y/n) ', default = 'y')
args = parser.parse_args()

folder = "C0024" # must be "OO_output"
PWD = os.getcwd() + "/"
path = PWD + folder + "_output"
files2=glob.glob(path + "/*")
csvpath = os.path.join(path, folder) + ".csv"

total = 0
cnt = 1
width = 256
height = 256
x_gap = 30
y_gap = 30
thorn = 0
info = 'width={} \nheight={} \nx_gap={} \ny_gap={} \nthorn={}'.format(width, height, x_gap, y_gap, thorn)

print('--directories to be cropped--')

for cname in files2:
	if cname.endswith("_checked"):
		print(os.path.basename(cname))
		total+=1

print('-----------------------------')
print('-----Total:{} directories-----'.format(total))


for cname in files2:
	break_check2 = 0
	
	if not cname.endswith("_checked"):
		break_check2=1
	
	if break_check2 == 0:
		
		if args.change_name == 'n':
			shutil.copytree(cname, path + "/" + os.path.basename(cname) + "_" + str(width) + "_" + str(height) + "_" + str(x_gap) + "_" + str(y_gap) + "_" + str(thorn))
			cname = path + "/" + os.path.basename(cname) + "_" + str(width) + "_" + str(height) + "_" + str(x_gap) + "_" + str(y_gap) + "_" + str(thorn)
		
		csvimgcnt=0
		row = 0
		start_of_newimg_index = 0
		df = pd.read_csv(csvpath, index_col=0)
		for pt in range(len(df)): # http://www.kisse-logs.com/2017/04/11/python-dataframe-drop/
			if df.loc[pt, 'image'] == cname[:-8]:
				csvimgcnt+=1
				row=pt
		start_of_newimg_index = row - csvimgcnt + 1

		basename = os.path.basename(cname)
		#crpimg = cv2.imread(cname + "/" + basename[:-12] + "_annotated.jpg") #this is for checking. DO NOT DELETE IT.
		crpimg = cv2.imread(cname + "/LAST/0.jpg")
		pbar = tqdm(total=int(((crpimg.shape[0]-height-100)/y_gap)*((crpimg.shape[1]-width-100)/x_gap)))
		pbar.set_description("{}: {}".format(cnt, os.path.basename(cname)))
		cnt+=1
		
		with open(cname + "/crop_info.txt", mode='w') as f:
			f.write(info)
		
		for i in range(50, crpimg.shape[0]-height-50, y_gap): # y
			for j in range(50, crpimg.shape[1]-width-50, x_gap): # x
				cropped=crpimg[i:i+height, j:j+width]
				df = pd.read_csv(csvpath, index_col=0)
				for pt in range(start_of_newimg_index, start_of_newimg_index+csvimgcnt, 1): # http://www.kisse-logs.com/2017/04/11/python-dataframe-drop/
					if df.loc[pt, 'image'] == cname[:-8]:
						pt_x = df.loc[pt, 'x']
						pt_y = df.loc[pt, 'y']
						if j + thorn <= pt_x and pt_x <= j + width - thorn and i + thorn <= pt_y  and pt_y <= i + height - thorn:
							cv2.imwrite(cname + "/" + os.path.basename(cname) + "_" + str(j) + "_" + str(i) + ".jpg", cropped)
							crpdcsv = pd.read_csv(os.path.join(cname, basename[:-8] + ".csv"), index_col=0)
							series = pd.Series([os.path.join(path, os.path.basename(cname) + "_" + str(j) + "_" + str(i) + ".jpg"), pt_x-j, pt_y-i], index=crpdcsv.columns)
							crpdcsv = crpdcsv.append(series, ignore_index=True)
							crpdcsv.to_csv(os.path.join(cname, basename[:-8] + ".csv"))
						else: #no human data
							cv2.imwrite(cname + "/" + os.path.basename(cname) + "_" + str(j) + "_" + str(i) + ".jpg", cropped)
							crpdcsv = pd.read_csv(os.path.join(cname, basename[:-8] + ".csv"), index_col=0)
							series = pd.Series([os.path.join(path, os.path.basename(cname) + "_" + str(j) + "_" + str(i) + ".jpg"), -1, -1], index=crpdcsv.columns)
							crpdcsv = crpdcsv.append(series, ignore_index=True)
							crpdcsv.to_csv(os.path.join(cname, basename[:-8] + ".csv"))
							break
				pbar.update(1)
		pbar.close()
		
		if args.change_name == 'y':
			os.rename(cname, cname[:-8]+"_cropped")
				
	
