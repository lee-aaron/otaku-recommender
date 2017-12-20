# [START app]
import logging

from flask import Flask, render_template, request
from flask.json import jsonify
# import source.ratings as ratings
# import source.mal_crawler as mal_crawler

app = Flask(__name__)

@app.route('/')
def main():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')

@app.route('/anime-recommendation')
def anime_recommendation():
    """Return anime recommendation."""
    return render_template('anime-recommendation.html')

@app.route('/about')
def about():
    """Return about."""
    return render_template('about.html')

@app.errorhandler(404)
def error(e):
    """Return a 404."""
    return render_template('404.html')


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]