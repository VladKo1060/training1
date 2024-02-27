from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')   # endpoint
def hello():      # функция представления

    return f"""
    <!DOCTYPE html>
    <html lang = "ru">
    <head>
        <meta charset = "UTF-8">
        <title>__name__</title>
    </head>
    <body>
        <h1>Тестовый сайт!!!</h1>
        <text>Это написано в теге текст</text>
        <a href={url_for("index")}>индекс</a>
        <a href={url_for("base")}>это база</a>
        <a href={url_for("start")}>старт</a>
        <a href={url_for("form")}>Форма</a>
        <a href={url_for("login")}>лог ин</a>
        <p><img src={url_for('static', filename="img.jpg")} alt="Описание изображения"></p>
    </ body>
    </ html>
    """


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/day-15/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.mathod == 'POST':
        print(request.form)
    return render_template(f'form.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
    return render_template(f'form_login.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
