from flask import Flask
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    f = open('words.txt', 'r')
    words = []
    for word in f:
        words.append(word.upper())
    f.close()
    obj = {
        'result': random.choice(words).rstrip()
    }
    return obj