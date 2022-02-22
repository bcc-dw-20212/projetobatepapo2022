from flask import Flask, jsonify, redirect, render_template, request
from datetime import datetime, timezone, timedelta


conversas = {}


app = Flask(__name__)

@app.get('/chat')
def raiz():
    resp = {'conversas': conversas}
    return jsonify(resp)

@app.post('/chathtml/<conv>/<autor>')
def conversa(conv, autor):
    fala = request.form['fala']
    conversas[conv].append({'autor': autor, 'fala': fala, 'timestamp': datetime.now(timezone(-timedelta(hours=3))).strftime('%d/%m/%Y %H:%M')})
    return redirect(f'/chathtml/{conv}/{autor}')


@app.get('/chathtml/<conv>/<autor>')
def html(conv, autor):
    if not conv in conversas:
        conversas[conv] = []
    return render_template('chat.html', autor=autor, conversas=conversas[conv], conversa=conv)

