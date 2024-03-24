import streamlit as st
import requests
import time


def submit_question_and_documents():
    st.title('Submit Question and Documents')
    question = st.text_input('Enter your question:')
    document_urls_input = st.text_area('Enter document URLs (one per line):')
    document_urls = [url.strip() for url in document_urls_input.split('\n') if url.strip()]

    if document_urls:
        st.write("Uploaded Document URLs:", document_urls)
    submit_button = st.button('Submit')
    url = 'http://localhost:8080//submit_question_and_documents'
    if submit_button:
        data = {
            "question": question,
            "documents": document_urls,
            "autoApprove": True
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            st.write("Response:", response.text)
        else:
            st.write("Failed to submit question and documents. Status code:", response.status_code)

def display_dynamic_panels(data):
    st.title('Extracted Facts')
    url = 'http://localhost:8080/get_question_and_facts'
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
        # print(data,type(data))
        question = data.get('question')
        st.subheader(question)
        status = data.get('status')
        while status=="processing" and response.status_code==200:
            time.sleep(2)
            response = requests.get(url)
            data = response.json()
            # print(data)
            status = data.get('status')
        if response.status_code==200 and status=="done":
            facts_by_day = data.get('factsByDay', {})
            if not facts_by_day:
                st.write('No facts available.')
            else:
                for date, facts in facts_by_day.items():
                    st.subheader(date)
                    for fact in facts:
                        st.write(f"- {fact}")
    else:
        st.write(f"Failed to retrieve data. Status code: {response.status_code}")

    

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio('Go to', ['Submit Question', 'Dynamic Panels'])

    if selection == 'Submit Question':
        submit_question_and_documents()
    elif selection == 'Dynamic Panels':
        json_data = [...]  # Load your JSON data here
        display_dynamic_panels(json_data)

if __name__ == "__main__":
    main()