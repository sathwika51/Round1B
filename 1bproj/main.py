import os
import json
import fitz
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load persona
with open("persona.json", "r") as f:
    persona_data = json.load(f)

persona = persona_data["persona"]
job_to_be_done = persona_data["job_to_be_done"]

# Load PDFs
input_folder = "input_files"
pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

pdf_contents = []

for pdf_file in pdf_files:
    doc = fitz.open(os.path.join(input_folder, pdf_file))
    for page_num in range(len(doc)):
        text = doc.load_page(page_num).get_text().strip()
        if text:
            pdf_contents.append({
                "document": pdf_file,
                "page_number": page_num + 1,
                "text": text
            })
    doc.close()

# Score relevance
page_texts = [p["text"] for p in pdf_contents]
job_corpus = [job_to_be_done] + page_texts
vectorizer = TfidfVectorizer(stop_words="english")
tfidf = vectorizer.fit_transform(job_corpus)
similarities = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

# Attach scores
for i, score in enumerate(similarities):
    pdf_contents[i]["score"] = float(score)

# Sort top 5
top_pages = sorted(pdf_contents, key=lambda x: x["score"], reverse=True)[:5]

# Final JSON format
final_output = {
    "metadata": {
        "input_documents": pdf_files,
        "persona": persona,
        "job_to_be_done": job_to_be_done,
        "processing_timestamp": datetime.now().isoformat()
    },
    "extracted_sections": [],
    "sub_section_analysis": []
}

for i, page in enumerate(top_pages):
    section_title = page["text"].split('\n')[0][:60]  # first line as title
    final_output["extracted_sections"].append({
        "document": page["document"],
        "page_number": page["page_number"],
        "section_title": section_title,
        "importance_rank": i + 1
    })

    final_output["sub_section_analysis"].append({
        "document": page["document"],
        "page_number": page["page_number"],
        "refined_text": page["text"][:500]  # first 500 characters as refined content
    })

# Save JSON to /output/result.json
os.makedirs("output", exist_ok=True)
with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=2)

print("✅ Result saved to output/result.json")
