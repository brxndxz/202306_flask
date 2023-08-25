from flask import Flask, render_template, redirect, request, session, key_name
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html" )
    
@app.route('/process', methods=['POST'])
def process(key_name):
    print("Got Post Info")
    if 'key_name' in session:
        print('la llave existe!')
    else:
        print("la llave 'key_name' NO existe")

    return redirect('/index.html')

if __name__ == "__main__":
    app.run(debug=True)