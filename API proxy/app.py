from flask import *
import requests

app = Flask(__name__)

@app.route("/")

def message():

    data={"message":"Api utilisateur"}

    return jsonify(data)

@app.route("/speech",methods = ['POST'])

def speech():
    if request.method == 'POST':
        texte = request.args.get('tx')
        langue = request.args.get('lg')
        url = "http://api.voicerss.org/?key=75d6d2b404324de599f13265388ae794&c=WAV&hl="+langue+"&src="+texte
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)