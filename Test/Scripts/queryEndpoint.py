import requests


url = 'http://localhost:8080//submit_question_and_documents'

data = {
    "question": "What are our product design decisions?",
    "documents": [
        "http://localhost:8000/LLMLogsInformationExtractor/Test/Files/call_log_20240314_104111.txt",
        "http://localhost:8000/LLMLogsInformationExtractor/Test/Files/call_log_20240315_104111.txt",
        "http://localhost:8000/LLMLogsInformationExtractor/Test/Files/call_log_20240316_104111.txt"
    ],
    "autoApprove": True
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Response:", response.text)
else:
    print("Failed to submit question and documents. Status code:", response.status_code)