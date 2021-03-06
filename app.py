from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)


@app.route('/translate', methods=['POST'])
def translate_text():
    lang = request.args.get('lang')
    text = request.data.decode()
    output_text = ""
    translator = GoogleTranslator(source='auto', target=lang)

    text_array = re.split("<<break>>", text.replace(".", ".<<break>>"))

    translated_array = translator.translate_batch(text_array)

    for paragraph in translated_array:
        output_text = output_text + paragraph

    return jsonify(output_text)


if __name__ == '__main__':
    app.run()
