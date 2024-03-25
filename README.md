# Call Log Facts Generator

This repository contains a Python application powered by a Language Model (LLM) that extracts relevant facts from a list of call logs based on user-provided questions. The backend is built using Flask and housed in `backend.py`, while the frontend is implemented in `app.py` using Streamlit. The core functionality for information extraction resides in `informationExtract.py`.

**Note:** The `.env` file storing the OpenAI API key is not included in this repository. You will need to create your own `.env` file and add your API key. Ensure the `.env` file is stored in the project folder.
## File Structure

- **Prompts:** Contains text files storing different prompts for generating questions.
- **Test:** Includes test scripts and files necessary for testing the application.
  - **Files:** Holds test call log files and sample inputs for the frontend.
  - **Scripts:** Contains test scripts along with a file server code.
- **main.py:** Initiates all servers and the frontend, allowing for easy execution with a single command.

## Setup

1. Clone this repository to your local machine.
2. Ensure you have Python installed (version 3.6 or above).
3. Install the required dependencies by running:
```
pip install -r requirements.txt
```

## Usage

1. Run the backend server by executing `backend.py`:
```
python3 backend.py
```
2. Run the frontend server by executing `app.py`:
```
streamlit run app.py
```
3. You can run file server by executing `Test/Scripts/filerServer.py
`:
```
python3 Test/Scripts/filerServer.py
```

## How It Works

1. **Backend (`backend.py`):** 
- Provides the necessary APIs for communication between the frontend and the LLM model.
- Handles processing of the user's input, fetching call logs, and sending relevant facts back to the frontend.

2. **Frontend (`app.py`):** 
- Built using Streamlit, providing an intuitive interface for users to input questions and view extracted facts.
- Sends user queries to the backend and displays the extracted information.

3. **LLM Information Extraction (`informationExtract.py`):** 
- Contains the logic for extracting relevant facts from call logs based on user-provided questions.
- Utilizes a pre-trained language model to comprehend the questions and extract pertinent information.

