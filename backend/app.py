from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import pandas as pd
from surprise import Reader, Dataset
from surprise import SVD, evaluate
from collections import defaultdict

from account import Account

app = Flask(__name__)
CORS(app)

@app.route('/recommend')
def getRecommendation():
  username = request.args.get('username')
  
  username = username.encode('utf-8')
  if username.count(';') > 0:
      return "Username Error"

  return jsonify(get_recommendation(username))

def get_top_n(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

def get_recommendation(user):

    conn = pymysql.connect(Account.link,
        Account.user, Account.password, Account.db, charset="utf8mb4")

    df = pd.read_sql_query('SELECT * FROM USERS', conn)

    if ( df.empty ):
        return "Error - empty DF"

    conn.close()

    # Anime can be rated from 1 - 10
    data = Dataset.load_from_df(df,Reader(rating_scale=(1,10)))

    data.split(n_folds=10)
    algo = SVD()

    trainset = data.build_full_trainset()
    algo.train(trainset)

    # predict ratings for all pairs (user, score) that are NOT in the train set
    testset = trainset.build_anti_testset()
    predictions = algo.test(testset)

    # Get top 15 predictions
    top_n = get_top_n(predictions, n=15)

    if top_n.get(user) is None:
        return "Error - cannot find User"

    return [iid for (iid, _) in top_n.get(user)]
    # print(user, [iid for (iid, _) in top_n.get(user)])

    #for uid, user_ratings in top_n.items():
    #   print(uid, [iid for (iid, _) in user_ratings])
  
if __name__ == '__main__':
  app.run()