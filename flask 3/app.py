from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Witaj w Flask!')

@app.route('/about')
def about():
    imie = 'Diana'
    nazwisko = 'Samiczak'
    wiek = 23
    return render_template('about.html', imie=imie, nazwisko=nazwisko, wiek=wiek)

if __name__ == '__main__':
    app.run(debug=True)
