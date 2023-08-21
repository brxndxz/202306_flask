from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = 'encriptar esto'

@app.route('/')
def tablero1():
    return render_template('tablero.html', x=8, y=8)

@app.route('/play/4')
def playx():
    return render_template('tablero.html', x = 4, y = 8)

@app.route('/play/<int:x>')
def playy(x):
    return render_template('tablero.html', x = x, y = 1)

@app.route('/play/<int:x>/<int:y>')
def play_another(x, y):
    return render_template('tablero.html', x = x, y=y)

if __name__=="__main__":    
    app.run(debug=True) 