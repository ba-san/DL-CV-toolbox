import os
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import precision_recall_fscore_support
global fig_mx
global train_acc, train_loss, test_acc, test_loss, whether_first

train_accs = []
train_losses = []
test_accs = []
test_losses = []
epochs = []
whether_first = 1

def draw_graph(epoch_all, epoch_now, train_acc, train_loss, test_acc, test_loss, training_name, save_place=None):
	global whether_first, fig1, fig2
	train_accs.append(train_acc)
	train_losses.append(train_loss)
	test_accs.append(test_acc)
	test_losses.append(test_loss)
	epochs.append(epoch_now)
	
	if whether_first == 0:
		plt.close(fig1)
		plt.close(fig2)
	
	fig1 = plt.figure()
	plt.ylim(0.45, 1.0)
	plt.plot(epochs, train_accs, 'bo', label='Training acc')
	plt.plot(epochs, test_accs, 'b', label='Test acc')
	plt.title('Training and test accuracy; '+ training_name)
	plt.legend()
	
	fig2 = plt.figure()
	plt.plot(epochs, train_losses, 'ro', label='Training loss')
	plt.plot(epochs, test_losses, 'r', label='Test loss')
	plt.title('Training and test loss; ' + training_name)
	plt.legend()
	
	plt.pause(0.1)
	
	whether_first = 0
	
	#if epoch_now >= epoch_all-1:
	fig1.savefig('Training and test accuracy; '+ training_name)
	fig2.savefig('Training and test loss; ' + training_name)
	fig1.savefig(save_place + 'Training and test accuracy; '+ training_name)
	fig2.savefig(save_place + 'Training and test loss; ' + training_name)
		
def draw_graph_regress(epoch_all, epoch_now, train_loss, test_loss, training_name, save_place=None):
	global whether_first, fig, ymax_regress
	train_losses.append(train_loss)
	test_losses.append(test_loss)
	epochs.append(epoch_now)
	
	if whether_first == 0:
		plt.close(fig)
	else:
		ymax_regress = min(50.0, train_loss)
	
	fig = plt.figure()
	plt.ylim(0.0, ymax_regress)
	plt.plot(epochs, train_losses, 'navy', label='Training loss')
	plt.plot(epochs, test_losses, 'gold', label='Test loss')
	plt.title('Training and test loss; ' + training_name)
	plt.legend()
	
	plt.pause(0.1)
	
	whether_first = 0
	
	#if epoch_now >= epoch_all-1:
	fig.savefig(save_place + 'Training and test loss; ' + training_name)
    
def yyplot(y_obs, y_pred, binary_name, save_place=None):
    yvalues = np.concatenate([y_obs.flatten(), y_pred.flatten()])
    ymin, ymax, yrange = np.amin(yvalues), np.amax(yvalues), np.ptp(yvalues)
    fig = plt.figure(figsize=(8, 8))
    plt.scatter(y_obs, y_pred, color="gold")
    plt.plot([ymin - yrange * 0.01, ymax + yrange * 0.01], [ymin - yrange * 0.01, ymax + yrange * 0.01], color="navy")
    plt.xlim(ymin - yrange * 0.01, ymax + yrange * 0.01)
    plt.ylim(ymin - yrange * 0.01, ymax + yrange * 0.01)
    plt.xlabel('y_observed', fontsize=24)
    plt.ylabel('y_predicted', fontsize=24)
    plt.xticks( np.arange(0.0, 10.0, 1.0) )
    plt.yticks( np.arange(0.0, 10.0, 1.0) )
    plt.grid(b=True)
    if binary_name == True:
        plt.title('Train;Observed-Predicted Plot', fontsize=24)
    else:
	    plt.title('Test;Observed-Predicted Plot', fontsize=24)
    plt.tick_params(labelsize=16)

    if binary_name == True:
        fig.savefig('Train;Observed-Predicted-Plot.png')
        fig.savefig(save_place + 'Train;Observed-Predicted-Plot.png')
    else:
        fig.savefig('Test;Observed-Predicted-Plot.png')
        fig.savefig(save_place + 'Test;Observed-Predicted-Plot.png')
		
    plt.close(fig)

    return fig

    	
# https://funatsu-lab.github.io/open-course-ware/basic-theory/accuracy-index/#how-to-check-rmse-mae-yyplot		
# http://www.yamamo10.jp/yamamoto/comp/Python/library/Matplotlib/scatter/index.php
from scipy.stats import gaussian_kde

def yyplot_density(y_obs, y_pred, binary_name, save_place=None): #y_obs and y_pred must be numpy array
    xy = np.vstack([y_obs, y_pred])
    
    # if there's too many points, this will limit it.
    if xy.shape[1] > 100000:
        limit = xy.shape[1]/10
        xy = np.vstack([y_obs[:int(limit)], y_pred[:int(limit)]])
        
    z = gaussian_kde(xy)(xy)
    
    idx = z.argsort()
    x,y,z = y_obs[idx],y_pred[idx],z[idx]
    yvalues = np.concatenate([y_obs.flatten(), y_pred.flatten()])
    ymin, ymax, yrange = np.amin(yvalues), np.amax(yvalues), np.ptp(yvalues)
    fig = plt.figure(figsize=(8, 8))
    plt.scatter(x, y, c=z)
    plt.plot([ymin - yrange * 0.01, ymax + yrange * 0.01], [ymin - yrange * 0.01, ymax + yrange * 0.01], color="navy")
    plt.xlim(ymin - yrange * 0.01, ymax + yrange * 0.01)
    plt.ylim(ymin - yrange * 0.01, ymax + yrange * 0.01)
    plt.xlabel('y_observed', fontsize=24)
    plt.ylabel('y_predicted', fontsize=24)
    plt.xticks( np.arange(0.0, 10.0, 1.0) )
    plt.yticks( np.arange(0.0, 10.0, 1.0) )
    plt.grid(b=True)
    if binary_name == True:
        plt.title('Train;Observed-Predicted Plot', fontsize=24)
    else:
	    plt.title('Test;Observed-Predicted Plot', fontsize=24)
    plt.tick_params(labelsize=16)

    if binary_name == True:
        fig.savefig('Train;Observed-Predicted-Plot.png')
        fig.savefig(save_place + 'Train;Observed-Predicted-Plot.png')
    else:
        fig.savefig('Test;Observed-Predicted-Plot.png')
        fig.savefig(save_place + 'Test;Observed-Predicted-Plot.png')
		
    plt.close(fig)
    
    
# https;//scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py   
def plot_confusion_matrix(y_true, y_pred, classes, save_caption,
                          save_place=None,
                          normalize=False,
                          cmap=plt.cm.Blues
                          ):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    global fig_mx
    
    cm = confusion_matrix(y_true, y_pred)
    
    indices = precision_recall_fscore_support(y_true, y_pred, average="macro")
    precision = float(indices[0])
    recall = float(indices[1])
    fscore = float(indices[2])

    if normalize:                                          
        title = 'Normalized:precision={:.3f},recall={:.3f},fscore={:.3f}'.format(precision, recall, fscore)
    else:
        title = 'Not-normalized:precision={:.3f},recall={:.3f},fscore={:.3f}'.format(precision, recall, fscore)
    
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    fig_mx, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
   
    fig_mx.tight_layout()
    fig_mx.savefig(save_place + 'confusion_matrix;' + os.path.basename(save_caption) + '.png')
    fig_mx.savefig('confusion_matrix;' + os.path.basename(save_caption) + '.png')
    plt.close(fig_mx)
    return ax
	

if __name__ == '__main__': #this is for draw_graph debug
	
	epoch = 5
	train_acc4debug = [0.1, 0.2, 0.5, 0.6, 0.9]
	train_loss4debug = [5, 4, 3, 3, 1]
	test_acc4debug = [0.1, 0.3, 0.3, 0.5, 0.6]
	test_loss4debug = [5, 5, 4, 4, 3]
	
	
	for i in range(5):
		draw_graph(epoch, i, train_acc4debug[i], train_loss4debug[i], test_acc4debug[i], test_loss4debug[i], "debug")
	