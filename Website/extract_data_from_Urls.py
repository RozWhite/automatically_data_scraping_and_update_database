import os
# import glob
from dotenv import load_dotenv
load_dotenv()
from config import *
from langchain_community.document_loaders import WebBaseLoader
from get_Trevisto_Urls import urls
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
OPENAI_API_KEY=os.getenv("chatgpt_api_key")

# #print(len(urls))

###### Load and extract data from website 
loader = WebBaseLoader(urls)
docs = loader.load()
# #print(len(docs))

### remove all spaces
for i in range (len(docs)):
        docs[i].page_content=re.sub('\s+', ' ', docs[i].page_content)

### Create a function to prepare the data and upload to the Qdrant database
def database():
    
    embeddings=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    ###  Optional part
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100) #Chage the chunk_size and chunk_overlap as needed
    # texts = text_splitter.split_documents(docs)

        ####### connect to qdrant and create a new collection
    qdrant_client = QdrantClient(host=qdrant_host, port=qdrant_port)
    qdrant_client.delete_collection(collection_name="trevisto_web_auth")


    url = "http://localhost:6333"
    qdrant = Qdrant.from_documents(
        docs, 
        embeddings, 
        url=url,
        collection_name="trevisto_web_auth",
    )