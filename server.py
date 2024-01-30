from flask import Flask, request , render_template, session

app=Flask(__name__)

#home page (add content / promotions / culture es.food)
@app.route('/')
def home():
    return render_template('index.html')

#registrant entrance for social club
@app.route('/registra')
def registra():
    return render_template('registra.html')

#sesion scoring,orders & rewards
@app.route('/sesion')
def sesion():
    return render_template('sesion.html')

#our culture 
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# orders / payment / delivery / inventory  connected to a database
@app.route('/ordena')
def ordena():
    return render_template('ordena.html')

# google maps ubication / es.food culture Content
@app.route('/aqui')
def aqui():
    return render_template('aquiEstoy.html')