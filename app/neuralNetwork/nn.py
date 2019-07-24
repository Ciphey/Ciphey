import keras
from keras.models import Sequential

model = Sequential()

from keras.layers import Dense

model.add(Dense(units=64, activation='relu', input_dim=4))
model.add(Dense(units=4, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.compile(loss=keras.losses.sparse_categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))
# x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.
x_train = [[28, 16], [28, 13], [32, 19], [17, 51]]
y_train = [[1], [1], [0], [0]]
model.fit(x_train, y_train, epochs=5, batch_size=32)