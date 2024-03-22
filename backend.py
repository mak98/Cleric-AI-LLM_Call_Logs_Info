from flask import Flask, request, jsonify
from InformationExtract import LLMBot

bot=LLMBot()
app = Flask(__name__)

@app.route('/submit_question_and_documents', methods=['POST'])
def submit_question_and_documents():
    # Accept JSON input
    data = request.json
    question = data.get('question')
    documents = data.get('documents')
    data=bot.get_files(documents)
    return jsonify({
        "question": question,
        "status": "processing"
    })


@app.route('/get_question_and_facts', methods=['GET'])
def get_question_and_facts():

    return {}

if __name__ == '__main__':
    app.run(debug=True,port=8080)
