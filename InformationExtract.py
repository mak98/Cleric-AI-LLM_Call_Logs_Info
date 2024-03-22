from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate)
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
load_dotenv()

class OutputParser(BaseOutputParser):
    def parse(self,text:str):
        return text.strip().split(",")
class LLMBot():
    def __init__(self):
        self.data=""
        self.chat_model=ChatOpenAI()
        system_template="You are a Call log summary bot. You will be given call transcripts along with a question, you should should process the documents to extract facts relevant to the question. The application will store these facts along with the transcript. You will get all the information in store and will sugest if the facts tanken should be added, is some fact should be removed or modified?"
        human_template="{text}"
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
        #return self.data

# 






# chat_prompt=ChatPromptTemplate.from_messages([system_message_prompt,human_message_prompt])

# chain=LLMChain(
#     llm=chat_model,
#     prompt=chat_prompt,
#     output_parser=OutputParser()
# )



# print(chain.run("Audi cars"))