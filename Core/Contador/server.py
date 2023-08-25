from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta

# nuestra ruta de índice manejará la representación de nuestro formulario
@app.route('/')
def index():
    return render_template("index.html" )
    
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # aquí agregamos dos propiedades a la sesión para almacenar el nombre y el correo electrónico
    session['name'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')
    
# agregar este método
@app.route('/show')
def show_user():
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)

