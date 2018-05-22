#!/usr/bin/python3

from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()
model.add(Dense(3 ,input_shape=(2,), batch_size=50 ,activation='relu'))