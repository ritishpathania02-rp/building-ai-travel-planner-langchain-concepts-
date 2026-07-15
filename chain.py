from langchain_ollama import ChatOllama as co
from langchain_core.output_parsers import StrOutputParser
from  prompt import itinerary_prompt, budget_prompt, tips_prompt
llm = co(model = "llama3:latest", temperature = 0.3)
parser = StrOutputParser()
# we can also write StrOutputParser() instead of parser in our chain
chain1 = itinerary_prompt|llm|parser
chain2 = budget_prompt|llm|parser
chain3 = tips_prompt|llm|parser
