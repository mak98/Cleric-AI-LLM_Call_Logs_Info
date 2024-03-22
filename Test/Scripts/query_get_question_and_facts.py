import requests

def get_question_and_facts(url):
    response = requests.get(url)

    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Failed to get question and facts. Status code:", response.status_code)

if __name__=="__main__":
    url = 'http://localhost:8080/get_question_and_facts'
    get_question_and_facts(url)