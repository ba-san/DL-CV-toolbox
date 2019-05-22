# https://qiita.com/akabei/items/0eac37cb852ad476c6b9

import os 
import glob
import gspread
from oauth2client.service_account import ServiceAccountCredentials



#def update_gspread(dset_fname, train_acc, test_acc, train_loss, test_loss, epoch, otherparams):
def update_gspread(dset_fname, network_name, dataset_directory, train_acc, train_loss, test_acc, test_loss, epoch, otherparams=None):
	
	### open google spreadsheet ###
	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

	credentials = ServiceAccountCredentials.from_json_keyfile_name('something.json', scope)
	gc = gspread.authorize(credentials)
	wks = gc.open('something').sheet1


	### updating ###
	separate_dset_fname = dset_fname.split("_")
	dataset_name = separate_dset_fname[0]
	crp_x_length = separate_dset_fname[-8]
	crp_y_length = separate_dset_fname[-7]
	x_interval = separate_dset_fname[-6]
	y_interval = separate_dset_fname[-5]
	thorn = separate_dset_fname[-4]
	
	num_of_class = len(os.listdir(dataset_directory + "/" + dset_fname + "/train/"))
	
	resize_x_length = separate_dset_fname[-2]
	resize_y_length = separate_dset_fname[-1]
	
	train_list = glob.glob(dataset_directory + "/" + dset_fname + "/train/*/*.jpg", recursive=True)
	test_list = glob.glob(dataset_directory + "/" + dset_fname + "/test/*/*.jpg", recursive=True)
		
	
	new_row = [dataset_name, network_name, dataset_directory + "/" + dset_fname, train_loss, test_loss, train_acc, test_acc,
				len(train_list)+len(test_list), len(train_list), len(test_list), num_of_class,
				crp_x_length, crp_y_length, resize_x_length, resize_y_length, x_interval, y_interval, thorn, epoch]
				
	for i in range(len(otherparams)):
		new_row.append(otherparams[i])
			
	wks.append_row(new_row)
