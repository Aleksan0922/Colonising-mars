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


@app.route('/choice/<planet_name>')
def choice_planet(planet_name):
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Варианты выбора</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <p>Эта планета очень близко к Земле;</p>
                    <div class="alert alert-secondary" role="alert">
                        На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-success" role="alert">
                        На ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-light" role="alert">
                        На ней есть небольшое магнитное поле;
                    </div>
                    <div class="alert alert-warning" role="alert">
                        Наконец, она просто красива!;
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<level>/<rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Результаты</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <p>Претендента на участие в миссии {nickname}:</p>
                    <div class="alert alert-success" role="alert">
                        Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <p>Составляет {rating}!</p>
                    <div class="alert alert-warning" role="alert">
                        Желаем удачи!
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
