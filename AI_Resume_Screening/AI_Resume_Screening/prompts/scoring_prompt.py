from langchain_core.prompts import PromptTemplate

scoring_prompt = PromptTemplate(
    input_variables=["match_result", "job_description"],
    template="""
Based on the match result, give a score between 0 and 100.

Match:
{match_result}

Rules:
- Return ONLY a number
- Do NOT write code
- Do NOT explain
- Do NOT add extra text

Example:
85

Now give the score:
"""
)