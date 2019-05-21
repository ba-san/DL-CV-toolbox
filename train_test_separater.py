import os
import random
import shutil
import pandas as pd

random.seed(32)

#source = "name_of_folder"
source = "test"
max_num = 10000
PWD = os.getcwd()
root = os.path.join(PWD, source)
csvpath = os.path.join(root, source + ".csv")

os.rename(root, os.path.join(PWD, source + "_ori"))
os.makedirs(root)
trainf=os.path.join(root, "train")	
testf=os.path.join(root, "test")
os.makedirs(testf)

shutil.copytree(os.path.join(PWD, source + "_ori"), trainf)
files = os.listdir(trainf)

infocsv = pd.DataFrame(columns=['class', 'total', 'train', 'test'])
infocsv.to_csv(csvpath)

for category in files:
	
	os.makedirs(os.path.join(testf, category))
	images = os.listdir(os.path.join(trainf, category))
	total_num = len(images)
	
	if total_num > max_num:
		del_num = total_num - max_num
		random_delete_list = random.sample(range(total_num), k=del_num)
		
		for i in range(len(images)):
			if i in random_delete_list:
				os.remove(os.path.join(trainf, category + "/" + images[i]))
		
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
			

		
