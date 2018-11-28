#!/usr/bin/python3

import pandas as pd
import pymysql
from sklearn.model_selection import train_test_split
from account import Account

conn = pymysql.connect(Account.link, Account.user, Account.password, Account.db)

dataset = pd.read_sql_query('SELECT * FROM USERS', conn)

conn.close()

# Convert text strings to unique ints
dataset['USERHASH'] = dataset['USERHASH'].astype('category').cat.codes.values
dataset['ANIME'] = dataset['ANIME'].astype('category').cat.codes.values

train, test = train_test_split(dataset, test_size=0.2)

import keras
import matplotlib.pyplot as plt
import numpy as np
from keras.optimizers import Adam
from sklearn.metrics import mean_absolute_error

n_users, n_movies = len(dataset.USERHASH.unique()), len(dataset.ANIME.unique())
n_latent_factors_user = 5
n_latent_factors_movie = 8

movie_input = keras.layers.Input(shape=[1],name='Item')
movie_embedding = keras.layers.Embedding(n_movies + 1, n_latent_factors_movie, name='Movie-Embedding')(movie_input)
movie_vec = keras.layers.Flatten(name='FlattenMovies')(movie_embedding)
movie_vec = keras.layers.Dropout(0.2)(movie_vec)

user_input = keras.layers.Input(shape=[1],name='User')
user_vec = keras.layers.Flatten(name='FlattenUsers')(keras.layers.Embedding(n_users + 1, n_latent_factors_user,name='User-Embedding')(user_input))
user_vec = keras.layers.Dropout(0.2)(user_vec)

concat = keras.layers.merge([movie_vec, user_vec], mode='concat',name='Concat')
concat_dropout = keras.layers.Dropout(0.2)(concat)
dense = keras.layers.Dense(200,name='FullyConnected')(concat)
dropout_1 = keras.layers.Dropout(0.2,name='Dropout')(dense)
dense_2 = keras.layers.Dense(100,name='FullyConnected-1')(concat)
dropout_2 = keras.layers.Dropout(0.2,name='Dropout')(dense_2)
dense_3 = keras.layers.Dense(50,name='FullyConnected-2')(dense_2)
dropout_3 = keras.layers.Dropout(0.2,name='Dropout')(dense_3)
dense_4 = keras.layers.Dense(20,name='FullyConnected-3', activation='relu')(dense_3)

result = keras.layers.Dense(1, activation='relu',name='Activation')(dense_4)
adam = Adam(lr=0.005)
model = keras.Model([user_input, movie_input], result)
model.compile(optimizer=adam,loss= 'mean_absolute_error')

history = model.fit([train['USERHASH'], train['ANIME']], train['SCORE'], epochs=250, verbose=0)

print(history)

pd.Series(history.history['loss']).plot(logy=True)
plt.xlabel("Epoch")
plt.ylabel("Train Error")
#plt.show()

predictions = model.predict([test['USERHASH'], test['ANIME']])
print(mean_absolute_error(test['SCORE'], predictions))