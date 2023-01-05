from flask import *
import requests

app = Flask(__name__)

@app.route("/")

def message():

    data={"message":"Api utilisateur"}

    return jsonify(data)

@app.route("/speech",methods = ['POST'])

# FIXME:Recuperation dans le mauvais format
# Changement de langue ?
@app.route('/speech', methods=['POST'])
def text_to_speech():
    # Récupérez le paramètre de la demande
    text = request.form.get('text')

    # Envoi de la demande POST à l'API de synthèse vocale de VoiceRSS
    api_url = "https://api.voicerss.org/"
    api_key = "2bb4f37019574a49a19ed7dbbc8c8e39"
    language = "fr-fr"
    format = "wav"
    response = requests.post(api_url, data={
        "key": api_key,
        "src": text,
        "hl": language,
        "f": format
    })

    # Vérifiez si la demande a réussi
    if response.status_code == 200:
        # Renvoyez le fichier audio WAV
        return response.content, response.headers["Content-Type"]


def translate_text(text, to_language, api_key):
    base_url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": text,
        "target": to_language,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        translation = response.json()["data"]["translations"][0]["translatedText"]
        return translation
    else:
        return "Error: could not translate text."

@app.route("/translate", methods=["GET"])
def translate():
    text = request.args.get("text")
    api_key = request.args.get("YOUR_API_KEY")
    to_language = "fr"
    translation = translate_text(text, to_language, api_key)
    return translation

    print(response.json())


@app.route('/detect', methods=['POST'])
def detect_language():
    # Récupérez le paramètre de la demande
    text = request.form.get('text')

    # Envoi de la demande POST à l'API de détection de la langue
    api_url = "https://libretranslate.com/detect"
    response = requests.post(api_url, data={
        "text": text
    })

    # Vérifiez si la demande a réussi
    if response.status_code == 200:
        return response.json()

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)