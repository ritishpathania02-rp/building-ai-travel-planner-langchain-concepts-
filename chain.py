from langchain_ollama import ChatOllama as co
from langchain_core.output_parsers import StrOutputParser
from  prompt import ai_prompt
llm = co(model = "llama3:latest", temperature = 0.3)
parser = StrOutputParser()
# we can also write StrOutputParser() instead of parser in our chain
travelchain = ai_prompt|llm|parser
