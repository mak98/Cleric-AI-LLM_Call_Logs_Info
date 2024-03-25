import requests

def get_logs(url):
    response = requests.get(url)

    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Failed to get Logs. Status code:", response.status_code)

if __name__=="__main__":
    url = 'http://localhost:8080/get_logs'
    get_logs(url)