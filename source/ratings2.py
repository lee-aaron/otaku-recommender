#!/usr/bin/python3

from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np
import pymysql
from account import Account

conn = pymysql.connect(Account.link, Account.user, Account.password, Account.db)

dataset = pd.read_sql_query('SELECT * FROM USERS', conn)

X = dataset.iloc[:, :2].values
y = dataset.iloc[:, 2].values

conn.close()

labelencoder_X_1 = LabelEncoder()
X[:, 0] = labelencoder_X_1.fit_transform(X[:, 0])
labelencoder_X_2 = LabelEncoder()
X[:, 1] = labelencoder_X_2.fit_transform(X[:, 1])

#onehotencoder = OneHotEncoder(categorical_features = [1])
#X = onehotencoder.fit_transform(X).toarray()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

model = Sequential()
model.add(Dense(6, input_dim=2, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100, batch_size=10)

# calculate predictions
predictions = model.predict(X_test)

plt.plot(predictions)
plt.show()

# round predictions
#rounded = [round(x[0]) for x in predictions]
#print(rounded)