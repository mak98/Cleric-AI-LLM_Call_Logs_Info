from flask import Flask, request, jsonify
import json
from InformationExtract import LLMBot
from threading import Thread

bot=LLMBot()
app = Flask(__name__)

@app.route('/submit_question_and_documents', methods=['POST'])
def submit_question_and_documents():
    data = request.json
    bot.question = data.get('question')
    documents = data.get('documents')
    bot.get_files(documents)
    Thread(target=bot.get_summary).start()
    return jsonify({
        "question": bot.question,
        "status": "processing"
    })


@app.route('/get_question_and_facts', methods=['GET'])
def get_question_and_facts():
    if bot.summary_computed.is_set():
        out=bot.summary
    else:
        out={
        "question": bot.question,
        "status": "processing"
    }
    return jsonify(out)

if __name__ == '__main__':
    app.run(debug=True,port=8080)
