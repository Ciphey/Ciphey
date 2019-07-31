#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tensorflow.keras.callbacks import TensorBoard
import time
import numpy

from keras.callbacks import TensorBoard

tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0,
                          write_graph=True, write_images=False)

CATEGORIES = ["sha1", "md5", "sha256", "sha512", "caeser", "plaintext"]
CATEGORIES = [1, 2, 3, 4, 5, 6]

# minus 1 as it starts at 0
sha1 = 1
md5 = 2
sha256 = 3
sha512 = 4
caeser = 5
plaintext = 6


# In[11]:


import csv

with open('output.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)


# In[ ]:





# In[12]:


x = []
y = []
counter = 0.0
totals = 0.00
for item in your_list:
    counter = counter + 1
    y.append([item[-1]])
    # delete y from it
    del item[-1]
    # delete the plaintext
    del item[0]
    # delete the encrypted text
    del item[0]
    # delete the array (this was causing me problems)
    del item[2]
    item[0] = float(item[0])
    item[1] = float(item[1])
    try:
        item[2] = float(item[2])
        totals = totals + item[2]
    except ValueError as e:
        item[2] = float(totals / counter)
        
    x.append(item)
import pprint
x_train = numpy.asarray(x)
y_train = numpy.asarray(y)
print(x_train[0].shape)
pprint.pprint(x_train[0])
print(x_train[0])
print(list(x_train[0]))

DONOTCHANGE = x[0]


# In[15]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D, Reshape
from keras import backend as K


model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(3,)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Flatten())
model.add(Dense(6, activation='softmax'))

""""model = Sequential([Dense(128, activation='relu', input_shape=(3,)),
                    Flatten(),
                    Dense(128, activation='relu'),
                    Dense(6, activation='softmax'),])"""

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  
              metrics=['accuracy'])
model.fit(x_train, y_train, validation_split=0.2, epochs = 50, batch_size = 25)


# In[ ]:


model.save("NeuralNetworkModel.model")


# In[ ]:


new = []
new.append([17.0, 7.0, 0.0001298328198294165])
new = numpy.asarray(new)
#print(new.shape)
y = model.predict(new)


# In[ ]:


print(y_train[0])
numpy.set_printoptions(formatter={'float_kind':'{:f}'.format})
print(y.tolist()[0])
numpy.argmax(y.tolist()[0])


# In[ ]:


"""import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras import backend as K
#K.set_image_dim_ordering('th')

model = Sequential()
print(y_train.shape)
print(x_train.shape)
x_train = x_train.reshape((1, 190715, 3, 1))
y_train = y_train.reshape((1, 190715, 3))
y_train = y_train[0]


model.add(Conv2D(64, (3, 3), input_shape = (190715, 3, 1)))

model.add(tf.keras.layers.GlobalAveragePooling2D()) # change from flatten to GlobalAveragePooling2D()
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(6, activation=tf.nn.softmax))  # our output layer. 10 units for 10 classes. Softmax for probability distribution

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  
              metrics=['accuracy'])

print(y_train)

model.fit(x_train, y_train, epochs=1, batch_size = 25, validation_split=0.3)  # train the model"""


# In[ ]:


pip install keras


# In[ ]:




