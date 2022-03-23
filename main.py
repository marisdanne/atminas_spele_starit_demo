from flask import Flask, render_template, jsonify
import datubaze
import json

app = Flask('app')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/spele')
def spele():
  return render_template("spele.html")

@app.route('/pspele')
def pspele():
  return render_template("pspele.html")

@app.route('/top')
def top():
  return render_template("top.html")

@app.route('/topData')
def topData():
  data = datubaze.top()
  return jsonify(data)

@app.route('/postTop', methods=['POST'])
def postTop(dati):
  datiJson = json.loads(dati)
  datubaze.pievienot(datiJson)
  return "OK"

@app.route('/par')
def par():
  return render_template("par.html")  


app.run(host='0.0.0.0', port=8080)