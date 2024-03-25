import streamlit as st
import requests
import time

BACKEND_URL = 'http://localhost:8080'
def submit_question_and_documents():
    st.title('Submit Question and Documents')
    question = st.text_input('Enter your question:')
    document_urls_input = st.text_area('Enter document URLs (one per line):')
    document_urls = [url.strip() for url in document_urls_input.split('\n') if url.strip()]
    if not all(isinstance(url, str) and url.strip() for url in document_urls):
        st.error("Please enter valid URLs.")
        return
    submit_button = st.button('Submit')
    if submit_button:
        data = {
            "question": question,
            "documents": document_urls,
            "autoApprove": True
        }
        try:
            response = requests.post(f'{BACKEND_URL}/submit_question_and_documents', json=data)
            if response.status_code == 200:
                st.info(f'Question:{response.json().get("question")}')
            else:
                st.error(f"Failed to submit question and documents. Status code: {response.status_code}")
        except requests.ConnectionError:
            st.error("Failed to connect to the server. Please check if the backend server is running and the URL is correct")
def display_facts():
    st.title('Extracted Facts')
    try:
        logs = requests.get(f'{BACKEND_URL}/get_logs').json()
        response = requests.get(f'{BACKEND_URL}/get_question_and_facts')
        if response.status_code==200:
            data = response.json()
            question = data.get('question')
            st.subheader("Question: "+question)
            status = data.get('status')
            request_limit = 5
            while status=="processing" and response.status_code==200 and request_limit>0:
                time.sleep(2)
                response = requests.get(f'{BACKEND_URL}/get_question_and_facts')
                request_limit-=1
                data = response.json()
                status = data.get('status')
            if response.status_code==200 and status=="done":
                facts_by_day = data.get('factsByDay', {})
                if not facts_by_day:
                    st.write('No facts available.')
                else:
                    for (date, facts),log in zip(facts_by_day.items(),logs):
                        st.subheader(f'Facts at end of the day:{date}')
                        st.markdown(f"**URL:** {log['source']}")
                        st.code(log["content"],language="plaintext")
                        for fact in facts:
                            remove_fact = st.checkbox("", key=fact)
                            if not remove_fact:
                                st.write(f"{fact}")
                            if remove_fact:
                                st.markdown(f'<s>{fact}</s>', unsafe_allow_html=True)
                        
        elif response.status_code==204:
            st.error("No logs are uploaded, Please upload logs and Question to get started.")
        else:
            st.write(f"Failed to retrieve data. Status code: {response.status_code}")
    except Exception as e:
        st.error("error:"+str(e))
        submit_question_and_documents()
    

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio('Go to', ['Submit Question', 'Call Logs Summary'])

    if selection == 'Submit Question':
        submit_question_and_documents()
    elif selection == 'Call Logs Summary':
        display_facts()

if __name__ == "__main__":
    main()