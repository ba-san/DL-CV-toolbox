import os
import random
import shutil

random.seed(32)

#source = "name_of_folder"
source = "trial"
PWD = os.getcwd()
root = os.path.join(PWD, source)

os.rename(root, os.path.join(PWD, source + "_ori"))
os.makedirs(root)
trainf=os.path.join(root, "train")	
testf=os.path.join(root, "test")
os.makedirs(testf)

shutil.copytree(os.path.join(PWD, source + "_ori"), trainf)
files = os.listdir(trainf)

for category in files:
	os.makedirs(os.path.join(testf, category))
	images = os.listdir(os.path.join(trainf, category))
	total_num = len(images)
	train_num = len(images)-int(len(images)*0.2)
	test_num = int(len(images)*0.2)
	print('{}: total:{} train:{} test:{}'.format(category, total_num, train_num, test_num))
	
	random_list = [random.randint(0, total_num-1) for i in range(test_num)]

	for i in range(len(images)):
		if i in random_list:
			shutil.move(os.path.join(trainf, category + "/" + images[i]), os.path.join(testf, category))
		
