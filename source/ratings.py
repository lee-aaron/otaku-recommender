import sqlite3
import pandas as pd
from surprise import Reader, Dataset
from surprise import SVD, evaluate
from collections import defaultdict

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

    conn = sqlite3.connect('database/anime_storage')

    df = pd.read_sql_query('SELECT * FROM USERS', conn)

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
    top_n = get_top_n(predictions, n=10)

    # User is not on MAL/Database
    # Needs to move to top of method to be faster
    if user not in top_n:
        print user + ' not found in database'
        return

    print(user, [iid for (iid, _) in top_n.get(user)])

    #for uid, user_ratings in top_n.items():
    #   print(uid, [iid for (iid, _) in user_ratings])
