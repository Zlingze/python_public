from flask import Flask, render_template
from random import randint

app = Flask(__name__)

hero = ['黑暗之女', '狂战士', '正义巨像', '猩红收割者']

@app.route('/index')
def index():
    return render_template("index.html", hero=hero)

@app.route('/choujiang')
def choujiang():
    num = randint(0, len(hero)-1)
    return render_template("index.html", hero=hero, h=hero[num])

app.run(debug=True)