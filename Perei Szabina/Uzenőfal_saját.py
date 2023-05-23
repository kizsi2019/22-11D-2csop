from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Üdv a suliPY oldalán!'



@app.route('/contact')
def contact():
    return 'Jelentkezés a kurzusokra: info@sulipy.hu'


@app.route('/time')
def time():
    now = datetime.now()
    current_time = now.strftime('%H:%S')
    return 'A pontos idő' + current_time


if __name__ == '__main__':
    app.run(debug=True)
