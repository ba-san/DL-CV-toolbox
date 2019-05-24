import os
import glob
import shutil
from distutils.dir_util import copy_tree

PWD = os.getcwd() + "/"
files=glob.glob(PWD + "/*")
suffix = "256_256_30_30_0"
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
