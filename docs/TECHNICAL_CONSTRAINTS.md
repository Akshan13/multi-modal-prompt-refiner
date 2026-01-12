Technical Architecture
1. System Overview

The system follows a layered pipeline:

Input Files → Content Extraction → LLM Refinement → Validation → Structured Output

Each stage is independent and can be tested, debugged, or replaced without affecting the rest of the system. This makes the architecture easier to maintain and extend.

2. Data Flow

Step 1 – Input
The user provides one or more files through the CLI:

python src/main.py --text "input.txt" --pdf "spec.pdf" --image "sketch.png"


Step 2 – Extraction
Each file is processed by its dedicated extractor:

text_processor.py – reads plain text

pdf_processor.py – extracts content using PyMuPDF

docx_processor.py – reads Word documents

image_processor.py – performs OCR using EasyOCR

Step 3 – Normalization
All extracted content is merged into a single, labeled text block.

Step 4 – Refinement
The combined text is sent to the Google Gemini LLM, which converts it into a structured JSON format using a strict schema prompt.

Step 5 – Validation
The returned JSON is validated using Pydantic. Invalid or malformed responses are rejected.

Step 6 – Output
The validated result is printed or saved as a JSON file.

3. Input Processors

Each format has its own processor so failures in one format do not break the entire pipeline.

Text Processor

Reads UTF-8 encoded text files.

PDF Processor

Uses PyMuPDF (fitz) because it handles multi-page and complex layouts better than PyPDF2.

DOCX Processor

Uses python-docx to extract paragraph text from Word files.

Image Processor

Uses EasyOCR for OCR because:

It does not require system-level installation

Works well across fonts

Supports GPU acceleration if available

Handwriting is partially supported but not guaranteed.

4. LLM Refinement Layer

The LLM is used to perform semantic understanding, not raw parsing.

Rule-based methods (regex, keyword matching) fail on variations such as:

“$5000”

“five thousand”

“5K”

“around five grand”

An LLM can generalize across these formats.

The prompt enforces:

A fixed JSON schema

Default values like "not specified"

Strict output rules (“return only valid JSON”)

This prevents unstructured or hallucinated output from leaking into the system.

5. Multi-Modal Orchestrator

All extracted content is merged before calling the LLM.
This is a deliberate design choice:

Reason	Benefit
Single API call	Cheaper and faster
Full context	LLM can resolve conflicts between sources
Consistency	One unified output

Example:
If a PDF says the budget is $30K and an image says $35K, both appear in the same context so the LLM can note the conflict in extraction_notes.

6. Validation Layer (Pydantic)

Pydantic enforces:

Required vs optional fields

Allowed values (high | medium | low)

Type safety

Range constraints (e.g., confidence score between 0 and 1)

This prevents LLM mistakes from silently entering the output.

If validation fails, the system raises an error instead of returning bad data.

7. Error Handling Strategy

The system is designed to fail gracefully.

Scenario	Behavior
Missing file	Shows clear error
PDF/image failure	Continues with other files
LLM error	Raises contextual message
Invalid JSON	Rejected by Pydantic

This ensures partial inputs still produce usable results.

8. Performance

Typical processing times:

Step	Time
PDF/Text extraction	< 1 sec
OCR	1–3 sec
LLM call	2–5 sec

Multi-modal input usually completes in ~8–10 seconds.

9. Security Considerations

API keys stored in .env

No hard-coded credentials

File paths validated

LLM output never exposed without schema validation

10. Testing Strategy

Unit tests

Each processor tested independently

LLM mocked for deterministic results

Integration tests
Five end-to-end test cases covering:

Text only

PDF only

Image only

Mixed inputs

All formats combined

Cached outputs allow testing without consuming API quota.

11. Design Philosophy

This system is built around:

Modularity – easy to replace parts

Transparency – confidence and missing data exposed

Reliability – no unvalidated output

Extensibility – new formats can be added easily

12. Conclusion

The architecture converts chaotic, real-world inputs into consistent, validated, machine-readable prompts using a clean and explainable pipeline.
The goal is not just extraction — it is trustworthy structuring of information for AI systems.