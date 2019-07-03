import os
import glob
import shutil
import pandas as pd
from distutils.dir_util import copy_tree

PWD = os.getcwd() + "/"
files=glob.glob(PWD + "/*")
suffix = "384_384_30_30_0"
fname = os.path.basename(os.path.dirname(PWD))
datasetf = PWD + "/" + fname + "_" + suffix

if not os.path.exists(datasetf):
	os.makedirs(datasetf)

for f in files:
	if f.endswith(suffix) == True:
		print(f)
		copy_tree(f, datasetf)
		

[os.remove(delete) for delete in glob.glob(datasetf + "/*.txt")]
[os.remove(delete) for delete in glob.glob(datasetf + "/*.jpg")]
[os.remove(delete) for delete in glob.glob(datasetf + "/*.csv")]


classes = os.listdir(datasetf)

for classf in classes:
	if os.path.isfile(classf) or classf == 'LAST':
		continue
		
	PWD = datasetf + "/" + classf + "/"
	currentdname = os.path.basename(datasetf)
	csvfiles=glob.glob(PWD + "/*.csv")
	
	df = pd.DataFrame(columns=['image', 'x', 'y', 'num'])
	
	if os.path.exists(PWD + classf + "_" + currentdname + ".csv"):
		print('csv file already exists.')
		continue
	
	for csvfile in csvfiles:
		csvname = os.path.basename(csvfile)
		df_each = pd.read_csv(csvfile, index_col=0)
		df = df.append(df_each, ignore_index=True)
		
	df.to_csv(PWD + classf + "_" + currentdname + ".csv")
