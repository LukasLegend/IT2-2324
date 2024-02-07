from flask import Flask
import json
import requests

app = Flask(__name__)

base_url = "https://wttr.in/sandvika?format=j1"

@app.get("/")
def rute_index():
    res = requests.get(base_url)
    data = res.sjon
    akkurat_naa = data["current_condition"][0]["weatherDesc"][0]["value"]
    return "<h1>Hei på deg!</h1>"

app.run(port=5000, debug=True)