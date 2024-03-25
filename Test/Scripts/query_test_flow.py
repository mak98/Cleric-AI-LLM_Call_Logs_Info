from query_get_question_and_facts import get_question_and_facts
from query_submit_question_and_documents import submit_question_and_documents
from query_get_logs import get_logs
import time

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

submit_question_and_documents(url,data)

url = 'http://localhost:8080/get_logs'
get_logs(url)


url = 'http://localhost:8080/get_question_and_facts'
get_question_and_facts(url)

time.sleep(10)
get_question_and_facts(url)