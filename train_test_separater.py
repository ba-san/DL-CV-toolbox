import os
import glob
import random
import shutil
import pandas as pd

# https://note.nkmk.me/python-os-remove-rmdir-removedirs-shutil-rmtree/
def remove_glob(pathname, recursive=True):
    for p in glob.glob(pathname, recursive=recursive):
        if os.path.isfile(p):
            os.remove(p)            
            
random.seed(32)

#source = "name_of_folder"
max_num = 54
PWD = os.getcwd()
root = os.path.join(PWD, source)
csvpath = os.path.join(root, source + ".csv")

os.rename(root, os.path.join(PWD, source + "_ori"))
os.makedirs(root)
trainf=os.path.join(root, "train")	
testf=os.path.join(root, "test")
os.makedirs(testf)

## copy input folder to train file ##
shutil.copytree(os.path.join(PWD, source + "_ori"), trainf)
files = os.listdir(trainf)

infocsv = pd.DataFrame(columns=['class', 'total', 'train', 'test'])
infocsv.to_csv(csvpath)

for category in files:
	if os.path.exists(os.getcwd() + "/" + source + "/train/" + category + "/" + category + "_" + source + ".csv"):
		os.rename(os.getcwd() + "/" + source + "/train/" + category + "/" + category + "_" + source + ".csv", os.getcwd() + "/" + source + "/train/" + category + "/" + category + "_train.csv")
	remove_glob(os.getcwd() + "/" + source + "/train/" + category + "/*checked*.csv")
	
	os.makedirs(os.path.join(testf, category))
	images = os.listdir(os.path.join(trainf, category))
	total_num = len(images)
	
	df_category = pd.read_csv(os.getcwd() + "/" + source + "/train/" + category + "/" + category + "_train.csv", index_col=0)
	test_df = pd.DataFrame(columns=['image', 'x', 'y', 'num'])
	
	if total_num > max_num:
		del_num = total_num - max_num
		random_delete_list = random.sample(range(total_num), k=del_num)
		
		for i in range(len(images)):
			if i in random_delete_list:
				os.remove(os.path.join(trainf, category + "/" + images[i]))
				df_category = df_category[~df_category['image'].str.contains(images[i])] # removed several arrays from original.
				df_category = df_category.reset_index(drop=True)
		
		total_num = max_num
		images = os.listdir(os.path.join(trainf, category))
		
		
	train_num = len(images)-int(len(images)*0.2)
	test_num = int(len(images)*0.2)
	print('{}: total:{} train:{} test:{}'.format(category, total_num, train_num, test_num))
	
	df = pd.read_csv(csvpath, index_col=0)
	series = pd.Series([category, total_num, train_num, test_num], index=df.columns)
	df = df.append(series, ignore_index=True)
	df.to_csv(csvpath)

	random_move_list = random.sample(range(total_num), k=test_num)

	for i in range(len(images)):
		if i in random_move_list:
			shutil.move(os.path.join(trainf, category + "/" + images[i]), os.path.join(testf, category))
			df_4test = df_category[df_category['image'].str.contains(images[i])]
			df_category = df_category[~df_category['image'].str.contains(images[i])]
			df_category = df_category.reset_index(drop=True)
			test_df = test_df.append(df_4test)
			test_df = test_df.reset_index(drop=True)
			
	df_category.to_csv(os.getcwd() + "/" + source + "/train/" + category + "/" + category + "_train.csv")
	test_df.to_csv(os.getcwd() + "/" + source + "/test/" + category + "/" + category + "_test.csv")
			
			

		
