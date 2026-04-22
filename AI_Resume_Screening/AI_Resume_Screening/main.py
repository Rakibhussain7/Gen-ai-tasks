from cProfile import label
import os
from dotenv import load_dotenv

load_dotenv()

from chains.pipeline import run_pipeline
from PyPDF2 import PdfReader

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def run(label, resume, jd):
    print("\n" + "=" * 60)
    print(f"{label}")
    print("=" * 60)

    result = run_pipeline(resume, jd)
    save_output(result,label)

    import json

    print("\n👤 CANDIDATE DETAILS")
    print("-" * 40)
    print("Name:", result["extracted"].get("name", "N/A"))
    print("Email:", result["extracted"].get("email", "N/A"))

    print("\n📌 EXTRACTED INFORMATION")
    print("-" * 40)
    print(json.dumps(result["extracted"], indent=2))

    print("\n📊 MATCH ANALYSIS")
    print("-" * 40)
    print(json.dumps(result["matched"], indent=2))

    print("\n🎯 SCORE")
    print("-" * 40)
    print(result["score"])

    print("\n💡 EXPLANATION")
    print("-" * 40)
    print(result["explanation"])

    print("\n" + "=" * 60)

def main():
    print("\n🚀 AI Resume Screening System\n")

    jd = read_file("data/job_description.txt")

    choice = input("Enter resume PDF path (or press Enter for demo): ").strip()

    if choice:
        resume = read_pdf(choice)
        run("📄 Uploaded Resume", resume, jd)
    else:
        strong = read_file("data/resumes/strong.txt")
        avg = read_file("data/resumes/average.txt")
        weak = read_file("data/resumes/weak.txt")

        run("💪 Strong Candidate", strong, jd)
        run("⚖️ Average Candidate", avg, jd)
        run("❌ Weak Candidate", weak, jd)

import json

def save_output(result, label):
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write("\n" + "="*60 + "\n")
        f.write(label + "\n")
        f.write("="*60 + "\n\n")

        f.write("EXTRACTED:\n")
        f.write(json.dumps(result["extracted"], indent=2) + "\n\n")

        f.write("MATCH:\n")
        f.write(json.dumps(result["matched"], indent=2) + "\n\n")

        f.write("SCORE:\n")
        f.write(result["score"] + "\n\n")

        f.write("EXPLANATION:\n")
        f.write(result["explanation"] + "\n\n")

if __name__ == "__main__":
    main()