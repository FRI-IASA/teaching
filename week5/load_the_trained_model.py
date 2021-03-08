from tensorflow import keras
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



################# How to load the model ##############
loaded_model = keras.models.load_model('./my_first_model.h5')

predicitions_of_test_images = loaded_model.predict(x_test)

print (predicitions_of_test_images.shape)

print ('actual value of the first image in the test set', y_test[0,:])

print ('predicitions_of_test_images of the first image in the test set', predicitions_of_test_images[0,:])







