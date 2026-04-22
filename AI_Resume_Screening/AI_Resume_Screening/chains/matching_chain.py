from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts.matching_prompt import matching_prompt

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
parser = StrOutputParser()

matching_chain = matching_prompt | llm | parser