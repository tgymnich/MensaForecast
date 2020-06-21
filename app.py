import os
from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])



@app.route('/current/<mensa>')
def current(mensa):
    return "Current"


@app.route('/history/<mensa>/<date>')
def history(mensa, date):
    return "History"

@app.route('/prediction/<mensa>/<date>')
def history(mensa, date):
    return "Prediction"

if __name__ == '__main__':
    app.run()