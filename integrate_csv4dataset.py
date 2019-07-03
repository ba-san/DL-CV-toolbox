
import os
import glob
import pandas as pd

classes = os.listdir(os.getcwd())

for classf in classes:
	#if os.path.isfile(classf) or classf == 'LAST':
		#continue
		
	PWD = os.getcwd() + "/" + classf + "/"
	currentdname = os.path.basename(os.getcwd())
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
	
