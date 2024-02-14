import os
from flask import Flask, send_file, request


app = Flask(__name__)

@app.route("/")
def index():
    return send_file('web/index.html')

@app.route("/cadastro", methods=['POST'])
def cadastro():
    '''Um simples cadastro'''
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    email = request.form.get('email')

    return f"Cadastro realizado com sucesso! Nome: {nome}, Telefone: {telefone}, Email: {email}"

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 80)))
