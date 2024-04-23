from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, send


app= Flask(__name__)
app.config['SECRET'] = "scret!123"
socketio = SocketIO(app, cors_allowed_origins ="*")

@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)

    if message != "User connected!":
        send(message, broadcast= True)


nomes = []

@app.route('/')
def index():
    return render_template ("index.html", nome=nomes[0])

@app.route('/login')
def screen_login():
    return render_template("login.html")

@app.route('/acessoCliente', methods=["POST"])
def getData():
    nome = request.form.get('usuario')
    senha = request.form.get('senha')
    print(nome, senha)
    nomes.append(nome)
    return redirect("/") 


if __name__ == "__main__":
    socketio.run(app, host="192.168.10.89")