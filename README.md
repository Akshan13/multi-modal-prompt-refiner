> This project is a prototype built for a technical evaluation. It demonstrates system design,
information extraction, and prompt refinement — not a production-ready platform.

# Multi-Modal Prompt Refinement System

A Python-based system that processes diverse input types (text files, PDFs, Word documents, and images) and transforms them into standardized, structured prompts suitable for downstream AI processing.

## Problem Statement

Organizations and individuals receive project requirements in various formats - casual text descriptions, formal PDF specifications, hand-drawn sketches, or combinations thereof. This fragmentation makes it difficult to:
- Extract key information consistently
- Compare requirements across projects
- Feed data into automated systems
- Track completeness of requirements

This system solves these challenges by unifying multi-format inputs into a consistent, validated JSON structure.

## Key Features

- **Multi-format input support**: Text (.txt), PDF (.pdf), Word documents (.docx), and images (.png, .jpg)
- **Intelligent extraction**: Uses OCR for images and dedicated parsers for documents
- **LLM-powered refinement**: Leverages Google Gemini API to understand and structure natural language
- **Standardized output**: Consistent JSON schema regardless of input format
- **Validation system**: Rejects irrelevant or incomplete prompts
- **Confidence scoring**: Quantifies reliability of extracted information
- **Missing data handling**: Explicitly tracks what information is absent
- **Graceful degradation**: Works even with incomplete inputs

## System Architecture

┌─────────────────────────────────────────────────────────────┐
│ INPUT LAYER │
│ Text Files │ PDF Docs │ Word Docs │ Images (OCR) │
└──────────────┴────────────┴─────────────┴──────────────────┘
↓
┌─────────────────────────────────────────────────────────────┐
│ PROCESSING LAYER │
│ Text Processor │ PDF Processor │ DOCX Processor │ Image │
│ │ │ │ Processor│
└─────────────────┴───────────────┴────────────────┴──────────┘
↓
[Combined Text]
↓
┌─────────────────────────────────────────────────────────────┐
│ REFINEMENT LAYER │
│ LLM-based Analysis (Google Gemini) + Validation │
└─────────────────────────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────────────┐
│ OUTPUT LAYER │
│ Structured JSON (Pydantic Model) │
└─────────────────────────────────────────────────────────────┘

##  Project Structure

multi-modal-prompt-refiner/
├── src/
│ ├── processors/ # Input format processors
│ │ ├── init.py
│ │ ├── text_processor.py # Plain text extraction
│ │ ├── pdf_processor.py # PDF parsing
│ │ ├── docx_processor.py # Word document parsing
│ │ └── image_processor.py # OCR-based extraction
│ ├── refiner/ # Core refinement logic
│ │ ├── init.py
│ │ ├── llm_refiner.py # LLM integration
│ │ └── multi_modal_refiner.py # Orchestration
│ ├── models/ # Data structures
│ │ ├── init.py
│ │ └── refined_prompt.py # Pydantic schema
│ └── main.py # CLI interface
├── data/
│ ├── samples/ # Example input files
│ └── test_cases/ # 5 demonstration scenarios
│ ├── test1_text_only/
│ ├── test2_pdf_only/
│ ├── test3_image_only/
│ ├── test4_text_image_combo/
│ └── test5_all_formats/
├── tests/ # Unit tests
├── docs/ # Documentation
│ ├── DESIGN_DECISIONS.md
│ ├── TECHNICAL_ARCHITECTURE.md
│ └── CONTRIBUTION_ANALYSIS.md
├── requirements.txt # Python dependencies
└── README.md # This file


### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://ai.google.dev/))

### Installation

1. **Clone the repository**
git clone https://github.com/Akshan13/multi-modal-prompt-refiner.git
cd multi-modal-prompt-refiner
Install dependencies

pip install -r requirements.txt
Set up environment variables

# Create .env file
copy .env.example .env

# Edit .env and add your API key
GOOGLE_API_KEY=your_gemini_api_key_here
Usage
Process Single File

# Text file only
python src/main.py --text "data/samples/project_description.txt"

# PDF only
python src/main.py --pdf "data/samples/requirements.pdf"

# Image only
python src/main.py --image "data/samples/sketch.png"
Process Multiple Files (Combined)

python src/main.py --text "input.txt" --pdf "spec.pdf" --image "notes.png"
Save Output to File

python src/main.py --text "input.txt" --output "output.json"
Run Test Cases

cd data/test_cases
python run_all_tests.py
This will execute all 5 demonstration scenarios and generate outputs.

# Output Schema
The system produces a standardized JSON structure with the following fields:

json
{
  "project_name": "string",
  "core_intent": {
    "primary_goal": "string",
    "target_users": "string",
    "problem_statement": "string"
  },
  "functional_requirements": [
    {
      "requirement": "string",
      "priority": "high|medium|low",
      "category": "string"
    }
  ],
  "technical_constraints": {
    "technology_stack": ["string"],
    "integrations": ["string"],
    "performance_requirements": ["string"],
    "security_requirements": ["string"]
  },
  "project_metadata": {
    "budget": "string",
    "timeline": "string",
    "team_size": "string"
  },
  "expected_deliverables": ["string"],
  "metadata": {
    "confidence_score": 0.0-1.0,
    "missing_information": ["string"],
    "extraction_notes": "string"
  }
}
# Key Features of the Schema
Core Intent: Captures the fundamental purpose and problem being solved

Functional Requirements: Prioritized and categorized feature list

Technical Constraints: Stack, integrations, and performance needs

Metadata: Business constraints (budget, timeline, team)

Confidence Tracking: System reports how reliable the extraction is

Missing Information: Explicit list of gaps in the input

# Test Cases
Five diverse scenarios demonstrate system capabilities:

Test Case	Input Format	Project Type	Complexity
Test 1	Text only	Real Estate CRM	Simple
Test 2	PDF only	Drone Delivery System	Medium
Test 3	Image only	Smart Irrigation	Simple
Test 4	Text + Image	Recipe Recommendation App	Medium
Test 5	All formats	E-Learning Platform	Complex
Each test case includes:

Input files (in respective format)

Run script (run_test.py)

Generated output (output.json)

Cached output for testing without API calls

# Technology Stack
Python 3.8+: Core language

Google Gemini API: LLM for natural language understanding

PyMuPDF(fitz): PDF text extraction

python-docx: Word document processing

Pillow (PIL): Image handling

easyOCR: OCR for image text extraction

Pydantic: Data validation and schema enforcement

# Documentation
Detailed documentation is available in the docs/ folder:

DESIGN_DECISIONS.md - Problem-solving approach, schema rationale, and alternative approaches considered

TECHNICAL_ARCHITECTURE.md - System design, component interactions, and implementation details

CONTRIBUTION_ANALYSIS.md - Breakdown of AI-assisted vs. original analytical work

# Design Philosophy
Information Preservation: Extract maximum value from every input without loss

Graceful Degradation: Handle missing or incomplete data without failure

Consistency: Produce uniform output regardless of input format chaos

Transparency: Report confidence levels and missing information explicitly

Extensibility: Easy to add new input formats or output fields

Modularity: Each component is independently testable and maintainable

# Assumptions
All text inputs are in English

Images contain typed text (handwriting recognition limited)

Budget formats: "$X", "X dollars", "$X-$Y range"

Timeline formats: "X months", "X weeks", "Q1 2024"

File sizes are under 10MB

Internet connection available for LLM API calls

# Known Limitations
Language: Currently supports English only

Handwriting: Limited accuracy on handwritten notes

File Size: Large files (>10MB) may cause processing delays

API Dependency: Requires active internet and Gemini API access

Media Types: Does not process audio or video inputs

Real-time: Not optimized for real-time streaming inputs

LLM Dependency: LLMs are used for semantic understanding, but the system architecture,
validation, schema design, and control flow are deterministic and engineered by the author.



# Troubleshooting
Issue: "ModuleNotFoundError: No module named 'google.generativeai'"
Solution: Install dependencies with pip install -r requirements.txt

Issue: "API key not found"
Solution: Create .env file with GOOGLE_API_KEY=your_key

Issue: "Rate limit exceeded"
Solution:Wait for quota reset (midnight Pacific time)

Use cached outputs in test cases

Switch to Gemini 1.5 Flash model (higher rate limits)

Issue: "OCR not working"
Solution: Install Tesseract OCR:

Windows: Download from GitHub

Mac: brew install tesseract

Linux: sudo apt-get install tesseract-ocr

# License
This repository was created as part of a technical evaluation for a hiring process.
All rights to the code, design, and documentation remain with the author unless a
separate written agreement is made.

## Author
Akshan Khanna

Email: akshankhanna328@gmail.com

GitHub: @Akshan13

LinkedIn: Akshan Khanna

Built as part of a technical challenge to demonstrate multi-modal data processing, system design, and problem-solving capabilities.

Submission Date: January 12, 2026

***

## NOW DO THIS:

1. **Copy everything above**
2. **Open file:**
```powershell
cd D:\Projects\multi-modal-prompt-refiner
notepad README.md

 This project was created exclusively for evaluation purposes and should not be deployed
or commercialized without the author’s consent.
