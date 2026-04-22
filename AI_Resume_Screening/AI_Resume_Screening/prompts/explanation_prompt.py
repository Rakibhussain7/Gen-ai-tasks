from langchain_core.prompts import PromptTemplate

explanation_prompt = PromptTemplate(
    input_variables=["score", "match_result", "extracted_info"],
    template="""
Explain the score in 2-3 simple sentences.

Score: {score}
Match: {match_result}

Rules:
- Keep it short
- Do NOT write code
- Do NOT repeat input

Answer:
"""
)