from flask import Flask, jsonify, redirect, render_template, request

conversas = []


app = Flask(__name__)

@app.get('/chat')
def raiz():
    resp = {'conversas': conversas}
    return jsonify(resp)

@app.post('/chathtml/<autor>')
def conversa(autor):
    fala = request.form['fala']
    conversas.append({'autor': autor, 'fala': fala})
    return redirect(f'/chathtml/{autor}')


@app.get('/chathtml/<autor>')
def html(autor):
    return render_template('chat.html', autor=autor, conversas=conversas)

