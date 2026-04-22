from langchain_core.prompts import PromptTemplate

extraction_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract the following details from the resume.

Resume:
{resume}

Return ONLY valid JSON:
{{
  "name": "",
  "email": "",
  "skills": [],
  "tools": [],
  "experience": "",
  "domain": ""
}}

Rules:
- Do NOT assume missing values
- Do NOT add extra text
"""
)