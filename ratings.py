import sqlite3
import pandas as pd
from surprise import Reader, Dataset
from surprise import SVD, evaluate

conn = sqlite3.connect('database/anime_storage')

df = pd.read_sql_query('SELECT * FROM USERS', conn)

conn.close()

data = Dataset.load_from_df(df,Reader())

data.split(n_folds=10)
algo = SVD()
evaluate(algo, data, measures=['RMSE','MAE'])

trainset = data.build_full_trainset()
algo.train(trainset)

print(algo.predict('Bob','Kimi no Na Wa.',6))
