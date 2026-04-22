from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts.explanation_prompt import explanation_prompt

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
parser = StrOutputParser()

explanation_chain = explanation_prompt | llm | parser