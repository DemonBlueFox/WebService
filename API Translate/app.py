# Ne plus utiliser a supprimer

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    # Récupérez les paramètres de la demande
    text = request.form.get('text')
    source_language = request.form.get('source_language')
    target_language = request.form.get('target_language')

    # Envoi de la demande POST à l'API de traduction
    api_url = "https://libretranslate.com/translate"
    response = requests.post(api_url, data={
        "text": text,
        "source_language": source_language,
        "target_language": target_language
    })

    # Vérifiez si la demande a réussi
    if response.status_code == 200:
        # Renvoyez la réponse de l'API comme réponse de l'API Flask
        return response.json()
    else:
        return "Erreur: {}".format(response.status_code)

if __name__ == '__main__':
    app.run()