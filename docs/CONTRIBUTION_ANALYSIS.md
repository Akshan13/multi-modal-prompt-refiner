Contribution Analysis: AI Assistance vs. My Work
Purpose

This document explains how I used AI as a development tool while retaining full control over design, architecture, and engineering decisions.
AI helped me work faster and learn library usage, but all system design, trade-offs, and reasoning were done by me.

How I Used AI

I used AI in three main ways:

1. Understanding Tools and Libraries

AI helped me:

Learn how PyMuPDF extracts PDF text

Understand how EasyOCR works

Use Pydantic correctly

Structure Gemini API calls

I didn’t treat these as black boxes — I tested them on real files, observed failures, and adapted them to fit the system.

2. Writing and Cleaning Code

AI helped generate:

Boilerplate file handling

API call syntax

Initial drafts of functions

Help me understand library behavior and the flow of methods and functions

I reviewed, edited, and integrated all code into a single coherent system.
Many AI-generated parts were modified to:

Add error handling

Fit the modular architecture

Handle real-world edge cases

3. Improving Flow and Clarity

AI helped improve:

Prompt wording

Documentation phrasing

Section organization

However, all technical meaning, examples, and reasoning came from my own testing and decisions.

What I Designed and Decided
1. System Architecture

I designed the three-layer structure:

Input Processing → LLM Refinement → Validation


This separation makes the system:

Easier to test

More reliable

Easier to extend

This was not suggested by AI — it was a deliberate software engineering decision.

2. Output Schema

I designed the 7-field schema after testing multiple project examples.

Key decisions:

Splitting intent into goal, users, and problem

Using strings for budget and timeline

Adding priorities to requirements

Including a transparency layer (confidence, missing info, notes)

AI suggested larger and flatter schemas, but I simplified it based on what actually worked.

3. Confidence and Transparency Layer

I added:

confidence_score

missing_information

extraction_notes

This allows users to judge reliability instead of blindly trusting output.
This idea came from observing OCR and LLM errors during testing.

4. Multi-File Priority Logic

When multiple files disagree:

PDFs and DOCX are treated as more reliable

Images (OCR) are treated as less reliable

Conflicts are recorded instead of hidden.

5. Test Case Design

I created all 5 test scenarios myself:

Real estate CRM

Drone delivery

Smart irrigation

Recipe app

E-learning system

These were chosen to represent real-world diversity and complexity.

How I Worked With AI

My workflow was:

Define the problem I want to solve

Ask AI for examples or syntax

Implement in my system

Test with real inputs

Debug and refine

Decide what stays and what changes

AI helped me move faster — but it did not decide what the system should be.

What I Learned

LLMs are powerful but unreliable without validation

OCR errors must be communicated, not hidden

Simple schemas are more usable than complex ones

Transparency builds trust in AI systems

Final Perspective

AI was a productivity tool and a learning aid.
I was responsible for:

Architecture

Data model

Trade-offs

Testing strategy

Error handling

System behavior

AI helped me write code and improve clarity —
I decided what to build and why.