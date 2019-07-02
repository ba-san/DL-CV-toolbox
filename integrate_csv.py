
import os
import glob
import pandas as pd

PWD = os.getcwd() + "/"
currentfname = os.path.basename(os.getcwd())
currentdname = os.path.basename(os.path.dirname(os.getcwd()))
csvfiles=glob.glob(PWD + "/*.csv")

df = pd.DataFrame(columns=['image', 'x', 'y', 'num'])

if os.path.exists(PWD + currentfname + "_" + currentdname + ".csv"):
	print('csv file already exists.')
	exit()

for csvfile in csvfiles:
	csvname = os.path.basename(csvfile)
	df_each = pd.read_csv(csvfile, index_col=0)
	df = df.append(df_each, ignore_index=True)
	
df.to_csv(PWD + currentfname + "_" + currentdname + ".csv")
