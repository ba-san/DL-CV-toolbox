import numpy as np
import matplotlib.pyplot as plt

xs = np.arange(10)
handles = [] # A list of Artists (lines)
labels = ['red','green','blue'] # 簡単のため色＝ラベル名とする
for i in range(6):
    ys = (xs ** 2) / (i+1)
    line, = plt.plot( xs, ys, linestyle="solid", label='line{}'.format(i),color=labels[i//2])
    if i % 2 == 0: # 同色をまとめる
        handles.append(line)
#plt.legend()                  # そのまま
print(handles)
plt.legend( handles, labels)  # 色でまとめる
plt.show()
plt.pause(1)
