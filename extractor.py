import os
import random
import shutil
import pandas as pd

random.seed(42)

#source = "name_of_folder"
source = "train"
ratio = 0.25
PWD = os.getcwd()
root = os.path.join(PWD, source)

os.rename(root, os.path.join(PWD, source + "_ori"))
newf=os.path.join(PWD, source + "_extracted")

shutil.copytree(os.path.join(PWD, source + "_ori"), newf)
files = os.listdir(newf)

for category in files:
	
	images = os.listdir(os.path.join(newf, category))
	before_total_num = len(images)
	
	del_num = int(before_total_num*(1.0-ratio))
	random_delete_list = random.sample(range(before_total_num), k=del_num)
		
	for i in range(len(images)):
		if i in random_delete_list:
			os.remove(os.path.join(newf, category + "/" + images[i]))
		
	after_total_num = before_total_num - del_num
	images = os.listdir(os.path.join(newf, category))
		
	print('category:{} before:{} after:{}'.format(category, before_total_num, after_total_num))
		
