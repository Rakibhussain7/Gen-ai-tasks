from langchain_core.prompts import PromptTemplate

matching_prompt = PromptTemplate(
    input_variables=["extracted_info", "job_description"],
    template="""
Compare the candidate with the job description.

Candidate:
{extracted_info}

Job Description:
{job_description}

Return ONLY valid JSON:
{{
  "matched": [],
  "missing": []
}}

Do NOT add any extra text.
"""
)