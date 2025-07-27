# Approach Explanation – Round 1B: Persona-Driven Document Intelligence

## Objective

This solution is designed to assist in connecting the right information to the right user — aligning with the theme “Connect What Matters — For the User Who Matters.” Our goal is to intelligently extract and prioritize relevant content from a set of documents, guided by a specific persona and their job-to-be-done.

---

## Methodology

### 1. Input Handling

The system takes two main inputs:

- A folder (`input_files/`) containing 3–10 related PDF documents
- A `persona.json` file, which describes the user persona and their specific task

Each document may vary in content and domain — for instance, scientific research, financial reports, or educational material.

### 2. PDF Processing

We leverage **PyMuPDF** for parsing the documents efficiently. It allows extraction of raw text from each page of every PDF. Each extracted page is recorded along with its document name and page number.

This results in a linear text stream of all pages across documents, simplifying semantic analysis.

### 3. Semantic Relevance via TF-IDF

The essence of this challenge lies in **semantic understanding** — identifying which content matters most to the persona.

To accomplish this:

- We use **TF-IDF vectorization** (via `scikit-learn`) to represent text from each page, along with the persona’s `job_to_be_done`.
- We compute **cosine similarity** between the job description and every page’s text.
- This helps us score and rank how relevant each page is to the persona's task.

The top 5 most relevant pages are then selected for further analysis.

### 4. Output Generation

The final output is a structured JSON file that includes:

- **Metadata**: Input files, persona details, job-to-be-done, and processing timestamp
- **Extracted Sections**: Top 5 relevant sections, each with document name, page number, title (inferred from the first line), and rank
- **Sub-section Analysis**: Refined content (first 500 characters) from those sections

This format is fully aligned with the competition’s requirements and ready for evaluation.

---

## Performance Considerations

- The entire system runs on **CPU only**
- Processing completes within **60 seconds**, even for 5–7 documents with 50+ pages each
- The model and dependencies fit well under the **≤1GB size limit**
- All required packages are bundled via a compact **Dockerfile** for reproducibility

---

## Tools Used

- **Python 3.10**
- **PyMuPDF** for PDF parsing
- **scikit-learn** for TF-IDF and cosine similarity
- **Docker** for containerization

---

## Conclusion

The solution focuses on simplicity, clarity, and adaptability. By using efficient text extraction and semantic scoring, we ensure that each persona receives information that is truly relevant to their task — fulfilling the core idea of intelligent document personalization.

The pipeline is generalizable, efficient, and production-ready for similar real-world applications.
