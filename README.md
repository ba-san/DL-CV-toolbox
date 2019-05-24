# DL-CV-tools
useful tools for Deep Learning &amp; Computer Vision projects

**draw_learning_graph** - If you import this file when training, it will show you accuracy&loss graph dynamically.  

**image_resize** - create new image folder inside new "resize" directory, having resized images.  

**path_changer** - change path inside csv to fit your environment.  

**train_test_separater** - from folder which has imgs for each class, create dataset which has 20% test imgs and 80% train imgs, which is randomly selected from original folder.  

**integrate_img4dataset** - this is designed to use after train_test_separater.py. it will collect dataset which has designated suffix and integrate them to make one big dataset.  

**video2img** - from a video, it will create folder having every frame img.  

**write_gspread** - it will write final DL epoch result on google spreadsheet.  

## Workflow Example

### Image Preparation
**video2img** --you prepare some videos for image dataset.    
↓  
**integrate_img4dataset** -- With various imgs from some videos, create one big img folder for dataset.    
↓  
**train_test_separater** -- If you have created classes and sorted imgs above dataset accordingly, this script will make train&test folder automatically.  
↓  
**image_resize** -- If you wanna change image size, you can use this b4 training.  

If you wanna make dataset for object-counting, you can refer to this repository: [Count-Annotator2](https://github.com/ba-san/Count-Annotator2).

### Deep Learning
**draw_learning_graph** -- you can check accuracy&loss in real time.  
**write_gspread** -- you can check current learning status even on your smartphone!  

### Others
**path_changer** -- Well, I don't know, I hope this script meets your specific needs if any.  
