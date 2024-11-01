from app import app
from flask import request, render_template

@app.route("/")
def home():
    return render_template("index.html", par1="Seja bem vindo", par2="Cliente")

@app.route("/index")
def index():
    return render_template("index.html", par1="Seja bem vindo", par2="Cliente")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/autentica", methods=['POST'])
def autentica():
    user = request.form['user']
    password = request.form['pswrd']
    return render_template("usuario.html", user=user, password=password)

@app.route("/cadastrarCli", methods=['POST'])
def cadastra():
    name = request.form['name']
    cpf = request.form['cpf']
    user = request.form['user']
    password = request.form['pswrd']
    return render_template("usuario.html", name=name, cpf=cpf, user=user, password=password)