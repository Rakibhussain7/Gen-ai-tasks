# chains/pipeline.py

import json

from chains.extraction_chain import extraction_chain
from chains.matching_chain import matching_chain
from chains.scoring_chain import scoring_chain
from chains.explanation_chain import explanation_chain

def safe_json_load(text):
    try:
        text = text.strip()

        # Remove code block formatting if present
        if text.startswith("```"):
            text = text.split("```")[1]

        # Extract only JSON part
        start = text.find("{")
        end = text.rfind("}") + 1

        if start != -1 and end != -1:
            text = text[start:end]

        return json.loads(text)

    except Exception:
        return {}  # fallback if parsing fails

def run_pipeline(resume, job_description):

    extracted = extraction_chain.invoke(
        {"resume": resume},
        config={"tags": ["extraction"]}
    )
    extracted = safe_json_load(extracted)

    matched = matching_chain.invoke(
        {
            "extracted_info": extracted,
            "job_description": job_description
        },
        config={"tags": ["matching"]}
    )
    matched = safe_json_load(matched)

    score = scoring_chain.invoke(
        {
            "match_result": matched,
            "job_description": job_description
        },
        config={"tags": ["scoring"]}
    )

    # Clean score (remove spaces/newlines)
    score = score.strip()

    explanation = explanation_chain.invoke(
        {
            "score": score,
            "match_result": matched,
            "extracted_info": extracted
        },
        config={"tags": ["explanation"]}
    )

    explanation = explanation.strip()

    return {
        "extracted": extracted,
        "matched": matched,
        "score": score,
        "explanation": explanation
    }