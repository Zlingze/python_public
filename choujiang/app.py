from flask import Flask, render_template

app = Flask(__name__)

hero = ['黑暗之女', '狂战士', '正义巨像', '猩红收割者']

@app.route('/index')
def index():
    return render_template("index.html", hero=hero)

app.run(debug=True)