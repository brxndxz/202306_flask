from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    first_name = ""
    last_name = ""
    student_id = ""
    strawberry = ""
    raspberry = ""
    apple = ""
    return render_template("index.html", first_name = first_name, last_name  = last_name, student_id = student_id, strawberry = strawberry, raspberry = raspberry, apple = apple)

@app.route('/checkout', methods=['POST'])         
def checkout():
    items = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    
    print("Cobrando a", request.form['first_name']," ",request.form['last_name'], " por ", items, "frutas")
    print(request.form)

    return render_template("checkout.html", items = items)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    