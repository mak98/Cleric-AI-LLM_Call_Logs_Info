from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate)
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
load_dotenv()

json_output_sample="""

  "question": "Some question?",
  "factsByDay": 
    "YYYY-MM-DD": [
      "Fact",
      "Fact",
      "Fact"
    ],
    "YYYY-MM-DD":  [
      "Fact",
      "Fact",
      "Fact"
    ],
    "YYYY-MM-DD": [
      "Fact"
    ]
  ,
  "status": "done"

"""


class OutputParser(BaseOutputParser):
    def parse(self,text:str):
        return text.strip()
class LLMBot():
    def __init__(self):
        self.data=""
        self.question=""
        self.chat_model=ChatOpenAI()
        system_template="""You are a Call log summary bot. You are given call transcripts along with a question. You should process the documents to extract facts 
        relevant to the question. You should handle contradictions within and across documents, suggesting the addition, removal, or modification of facts as necessary.
        The output should be in the format of json,here is a sample output:"""+json_output_sample
        human_template="Use these call logs:{call_logs}\nQuestion:{question}"
        system_message_prompt=SystemMessagePromptTemplate.from_template(system_template)
        human_message_prompt=HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt=ChatPromptTemplate.from_messages([system_message_prompt,human_message_prompt])
        self.chain=LLMChain(
                            llm=self.chat_model,
                            prompt=chat_prompt,
                            output_parser=OutputParser()
                            )
    def get_files(self,url):
        loader = UnstructuredURLLoader(url)
        self.data = loader.load()
    
    def get_summary(self):
        print(self.data,self.question)
        out=self.chain.run(question=self.question,call_logs=self.data)
        return out

