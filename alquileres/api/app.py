from functionsDB import generate_chapters,list_available_chapters,list_rented_chapters,list_reserved_chapters,pay_chapter,rent_chapter
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Retorna la pagina index."""
    return render_template('/index.html')

@app.route('/about')
def about():
    """Retorna la pagina about."""
    return 'About Python Flask'

@app.route('/generate-chapters')
def generar():
    """Generar capitulos."""
    msj = generate_chapters()
    return msj

@app.route('/chapter/<state>')
def listar(state):
    """Retorna el listado de capitulos por estado."""
    if(state=='disponible'):
        lista = list_available_chapters()
        print(lista)
        return jsonify(lista)
    if(state=='reservado'):
        lista = list_reserved_chapters()
        print(lista)
        return jsonify(lista)
    if(state=='alquilado'):
        lista = list_rented_chapters()
        print(lista)
        return jsonify(lista)

@app.route('/chapter/<capitulo>/rent')
def alquilar(capitulo):
    """Retorna la pagina para alquilar capitulos."""
    msj = rent_chapter(capitulo)
    return msj

@app.route('/chapter/<capitulo>/pay/<prec>')
def pagar(capitulo,prec):
    """Retorna la pagina para pagar los capitulos."""
    msj = pay_chapter(capitulo,prec)
    return msj

if __name__ == "__main__":
    app.run(host='localhost', port='5000', debug=False)

