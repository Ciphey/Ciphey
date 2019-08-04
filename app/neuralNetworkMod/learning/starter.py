import tensorflow as tf
mnist = tf.keras.datasets.mnist # 28x28 images of hand-written digits 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
# input layer
model.add(tf.keras.layers.Flatten())

# hidden layers
# pass units to layer
# we're using 128 neurons in the layer
# pass the activation function
# relu is the default activation function
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

# output layer, the output layer will normally be the number of classifications
# in our case, that's 10
# we don't want to use relu, we want to use softmax for a probabiltiy distribution
# 10 numbers 0 - 9
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

# the loss metric is the degree of error
# what we got wrong
# a neural network doesnt attempt to optimise for accuracy, it's always trying to minimise loss
# the way you calculate loss can make a huge impact
# adam optimizer is default, it's most complex part of the entire neural network
# we could use stochastic gradient descent
# the most popular way to calculator loss is cross entropy
# for dogs and cats, we should use binary but we're using sparse
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# this is how we train it
model.fit(x_train, y_train, epochs=3)

# neural networks are great at ffitting, but they can overfit
# we want our model to generalise instead of memorising every single sample we pass
# to test overfitting we calculate the validation loss and validation accuracy

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

# save a model
model.save("epic_num.model")
new_model = tf.keras.models.load_model('epic_num.model')


predictions = new_model.predict(x_test)
import numpy as np
print(np.argmax(predictions[0]))