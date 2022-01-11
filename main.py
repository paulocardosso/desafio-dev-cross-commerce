from flask import Flask, jsonify, redirect
from src.extracao.numbers import extrair
from src.transformacao.ordenacao import quicksort

app = Flask(__name__)

"""
CARREGAMENTO DE DADOS ORDENADOS
"""
@app.route("/")
def hello_world():
    return redirect("/numerosordenados")

@app.get("/numerosordenados")
def get_numord():
    listcompleta = extrair()
    quicksort(listcompleta)
    numerosordenados = [
        {
            "numbers":
                listcompleta
        }
    ]
    return jsonify(numerosordenados)

if __name__ == '__main__':
    app.run(
        debug=True
    )