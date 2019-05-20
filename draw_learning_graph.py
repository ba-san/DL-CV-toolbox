import numpy as np
import matplotlib.pyplot as plt

global train_acc, train_loss, test_acc, test_loss, whether_first

train_accs = []
train_losses = []
test_accs = []
test_losses = []
epochs = []
whether_first = 1

def draw_graph(epoch_all, epoch_now, train_acc, train_loss, test_acc, test_loss, training_name):
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
	plt.ylim(0.0, 1.0)
	plt.plot(epochs, train_accs, 'bo', label='Training acc')
	plt.plot(epochs, test_accs, 'b', label='Test acc')
	plt.title('Training and test accuracy: '+ training_name)
	plt.legend()
	
	fig2 = plt.figure()
	plt.plot(epochs, train_losses, 'ro', label='Training loss')
	plt.plot(epochs, test_losses, 'r', label='Test loss')
	plt.title('Training and test loss: ' + training_name)
	plt.legend()
	
	plt.pause(0.1)
	
	whether_first = 0
	
	if epoch_now >= epoch_all-1:
		fig1.savefig('Training and test accuracy: '+ training_name)
		fig2.savefig('Training and test loss: ' + training_name)
	


if __name__ == '__main__': #this is for debug
	
	epoch = 5
	train_acc4debug = [0.1, 0.2, 0.5, 0.6, 0.9]
	train_loss4debug = [5, 4, 3, 3, 1]
	test_acc4debug = [0.1, 0.3, 0.3, 0.5, 0.6]
	test_loss4debug = [5, 5, 4, 4, 3]
	
	
	for i in range(5):
		draw_graph(epoch, i, train_acc4debug[i], train_loss4debug[i], test_acc4debug[i], test_loss4debug[i], "debug")
	
