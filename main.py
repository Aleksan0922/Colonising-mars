from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def u():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.
    <br>Человечеству мала одна планета.
    <br>Мы сделаем обитаемыми безжизненные пока планеты.
    <br>И начнем с Марса!
    <br>Присоединяйся!'''


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


@app.route('/image_mars')
def image_mars():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
