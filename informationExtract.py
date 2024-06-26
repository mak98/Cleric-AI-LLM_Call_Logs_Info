from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate)
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
from threading import Thread, Event
import json
load_dotenv()

class OutputParser(BaseOutputParser):
    def parse(self,text:str):
        return json.loads(text.strip())
class LLMBot():
    def __init__(self):
        self.data=""
        self.question=""
        self.chat_model=ChatOpenAI()
        system_template=open('Prompts/prompt1.txt', 'r').read()
        human_template="Use these call logs:{call_logs}\nQuestion:{question}"
        system_message_prompt=SystemMessagePromptTemplate.from_template(system_template)
        human_message_prompt=HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt=ChatPromptTemplate.from_messages([system_message_prompt,human_message_prompt])
        self.chain=LLMChain(
                            llm=self.chat_model,
                            prompt=chat_prompt,
                            output_parser=OutputParser()
                            )
        self.summary={}
        self.summary_computed = Event()
    def get_files(self,url):
        self.summary_computed.clear()
        self.summary={}
        loader = UnstructuredURLLoader(url)
        self.data = loader.load()
    
    def get_summary(self):
        print(self.data,self.question)
        self.summary=self.chain.run(question=self.question,call_logs=self.data)
        self.summary_computed.set()
    

