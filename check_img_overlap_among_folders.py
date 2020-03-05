import os, glob, shutil

source_imgs = glob.glob('./all/*')
object_imgs = glob.glob('./crowd_night (after_select)/*/*/*/*.jpg') # imgs in this folder will be moved.
#object_imgs = glob.glob('./crowd_night (after_select)/*/*/*.jpg') # imgs in this folder will be moved.
moved_directory = 'removed'
cnt = 0

if not os.path.exists(moved_directory):
	os.makedirs(moved_directory)

for object_img in object_imgs:
	overlap = 0
	for source_img in source_imgs:
		if os.path.basename(source_img)[:-12]==os.path.basename(object_img)[:-4]:
			overlap = 1
			
	if overlap==0: # only in object_imgs
		print('{}:{}'.format(cnt, os.path.basename(object_img)))
		cnt = cnt + 1
		shutil.move(object_img, os.path.join(moved_directory, os.path.basename(object_img)))
