from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.datasets import *
from keras.losses import *
from keras.optimizers import *
import keras
import numpy as np
import matplotlib.pyplot as plt




######## Loading data ######################

(x_train, y_train), (x_test, y_test) = mnist.load_data()  # Loading MNIST Dataset
print(x_train.shape)  # 60000*28*28
print(y_train.shape)  # 60000
print(x_test.shape)  # 10000*28*28
print(y_test.shape)  # 10000
print (type(x_train))


######### Reshaping data ##################

### Shaping the square shaped image into 1D data
x_train = x_train.reshape(60000, 784).astype('float32')
x_test = x_test.reshape(10000, 784).astype('float32')

### Dividing all image pixel values by the maximum, also called as normalization
x_train = x_train / 255
x_test = x_test / 255
# print(x_train)
# print(x_test)
# print(y_train[55])

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

print(y_train.shape)
print(y_test.shape)
#print (y_test[0,:])


########## Building the model ####################

model = Sequential()
model.add(Dense(512, activation='relu', input_dim=784))

model.add(Dense(256, activation='relu'))

model.add(Dense(10, activation='softmax'))

print (model.summary())





model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

history = model.fit(x_train, y_train, batch_size=128, epochs=1, verbose=1, validation_data=(x_test, y_test))

# evaluate the model
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)

print ('Accuracy is:', accuracy)
print ('loss is:',loss)


############ I want to save the model now #########

model.save('./my_first_model.h5')



################# How to load the model ##############
loaded_model = keras.models.load_model('./my_first_model.h5')

predicitions_of_test_images = loaded_model.predict(y_test)

print (predicitions_of_test_images.shape)
