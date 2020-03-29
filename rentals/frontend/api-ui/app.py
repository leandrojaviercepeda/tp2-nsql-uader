from flask import Flask, render_template, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def index():
    """Retorna la pagina index."""
    return render_template('/index.html')

@app.route('/pay')
def about():
    """Retorna la pagina para pagar."""
    return render_template('pay.html')

if __name__ == "__main__":
    app.run(host='localhost', port='5000', debug=False)

