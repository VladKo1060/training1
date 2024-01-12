from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello():

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
        <p><img src={{ url_for('static', filename="img.jpg" alt="Описание изображения"}}></p>
    </ body>
    </ html>
    """


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
