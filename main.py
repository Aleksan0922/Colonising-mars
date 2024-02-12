from flask import Flask
from flask import render_template, request

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

@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template('astronaut_selection.html')
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['mail'])
        print(request.form['educ'])
        print(request.form['prof'])
        print(request.form['gender'])
        print(request.form['motiv'])
        print(request.form['stay'])
    return render_template('astronaut_selection.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
