from flask import Flask, request, jsonify,make_response
import json
from informationExtract import LLMBot
from threading import Thread

bot=LLMBot()
app = Flask(__name__)

@app.route('/submit_question_and_documents', methods=['POST'])
def submit_question_and_documents():
    try:
        data = request.json
        if not data or 'question' not in data or 'documents' not in data:
                return make_response({"error": "Invalid request data"}, 400)
        bot.question = data.get('question')
        documents = data.get('documents')
        bot.get_files(documents)
        Thread(target=bot.get_summary).start()
        return jsonify({
            "question": bot.question,
            "status": "processing"
        })
    except Exception as e:
        return make_response({"error": str(e)}, 500)


@app.route('/get_question_and_facts', methods=['GET'])
def get_question_and_facts():
    try:
        if bot.data=="":
            return make_response({"message": "No data available"}, 204)
        if bot.summary_computed.is_set():
            out=bot.summary
        else:
            out={
            "question": bot.question,
            "status": "processing"
        }
        return jsonify(out)
    except Exception as e:
        return make_response({"error": str(e)}, 500)
@app.route('/get_logs', methods=['GET'])
def get_logs():
    logs=bot.data
    formatted_logs =[]
    for document in logs:
        document_json={}
        source_url = document.metadata.get('source', '')
        document_json["source"]=source_url
        document_json['content']= document.page_content
        formatted_logs.append(document_json)
    print(formatted_logs) 
    return jsonify(formatted_logs)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
