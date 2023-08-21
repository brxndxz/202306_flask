from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta

@app.route('/')         
def encuesta():
    return render_template("encuesta.html")
    
@app.route('/process', methods=['POST'])
def create_user():
    print("Got Post Info")
    location = ""
    language = ""
    # aquí agregamos dos propiedades a la sesión para almacenar el nombre y el correo electrónico
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['user_message'] = request.form['user_message']
    return redirect('/result')

@app.route('/result')
def result():
    print(request.form)
    return render_template("result.html")

if __name__=="__main__":   
    app.run(debug=True)    