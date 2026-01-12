Design Decisions and Rationale
1. Problem Understanding

This task required designing a system that can handle messy, real-world, multi-modal inputs (text, PDFs, images, and mixed formats) and convert them into a clean, consistent, machine-readable structure suitable for downstream AI systems.

In practice, real requirements rarely arrive in a single format. They may be:

Informal text descriptions

Formal PDF specifications

Screenshots or photos of sketches

Combinations of all of the above

The core challenge was to convert this unstructured and inconsistent information into a structured, reliable prompt representation without losing meaning or inventing missing data.

2. High-Level Solution

The system was designed as a layered pipeline:

Input Files → Content Extraction → Semantic Understanding (LLM) → Validation → Structured Output

This separation allows each stage to be independently tested, improved, or replaced. For example, OCR errors can be fixed without touching LLM logic, and schema changes can be made without reworking file parsers.

3. Schema Design Rationale

The refined prompt schema was designed to capture both technical and business context while remaining flexible enough for incomplete inputs.

Field 1: project_name

A simple string was chosen instead of a complex object. Real-world inputs rarely contain consistent naming structures, so a flexible single field preserves maximum information.

Field 2: core_intent (Goal, Users, Problem)

This was one of the most important design decisions.

A single sentence such as “Build a CRM” is not sufficient. Splitting intent into:

Primary goal

Target users

Problem being solved

forces clarity and makes downstream AI systems far more effective.

Field 3: functional_requirements

An array structure allows:

Prioritization

Categorization

Iteration for feature planning

The priority field enables distinction between critical features and optional enhancements, which is essential for MVP planning.

Field 4: technical_constraints

Technical constraints were grouped into:

Technology stack

Integrations

Performance

Security

These categories reflect how engineering teams think and allow different downstream systems (architecture planning, cost estimation, security review) to consume the data independently.

Field 5: project_metadata

Budget, timeline, and team size were stored as strings rather than numbers.

This was a deliberate choice because real-world inputs often use imprecise formats such as:

“$5K–$8K”

“around five thousand”

“Q2 2024”

Converting these into numbers would lose semantic meaning.

Field 6: expected_deliverables

A simple list of outputs (e.g., “mobile app”, “API”, “documentation”) keeps the structure flexible and human-readable.

Field 7: metadata (Transparency Layer)

This was a key design contribution.

The system explicitly reports:

A confidence score

Missing information

Extraction notes

This allows users to understand how reliable the output is instead of blindly trusting the AI. This transparency layer turns the system from a black box into an inspectable pipeline.

4. Architectural Decisions
Why Separate Processors

Each input type (text, PDF, image) has its own processor.
This allows failures in one format to be isolated without affecting the rest of the system and simplifies debugging and extension.

Why Use an LLM Instead of Rule-Based Parsing

Rule-based systems (regex, keyword matching) break easily when language changes.

For example:

“Budget is $5,000”

“Around five thousand dollars”

“Cost ~5K”

An LLM can generalize across these variations, making it far more reliable for semantic extraction despite the API cost.

5. Engineering Challenges Encountered

API Rate Limits
LLM rate limits required introducing cached outputs so test cases could be executed repeatedly without unnecessary API calls.

OCR Quality
OCR sometimes misinterpreted characters (e.g., “$35,000” as “$35,00O”). This motivated the inclusion of extraction_notes to surface uncertainty rather than hide it.

Conflicting Information
When different sources disagreed (e.g., budget in PDF vs image), the system prioritized structured documents and recorded the decision in the metadata notes.

6. AI Assistance vs Original Design
AI was used for:

Boilerplate code generation

API usage examples

Initial prompt drafts

I was responsible for:

Designing the 7-field schema

Deciding what information is mandatory vs optional

Designing the confidence and missing-data tracking

Defining validation rules

Creating the test case scenarios

The AI acted as a productivity tool, while all architectural and design decisions were human-driven.

7. Key Lessons

Simpler schemas are more robust than complex ones.

Missing information should be reported, not guessed.

Transparency is as important as accuracy.

8. Future Improvements

Interactive refinement when confidence is low

Improved OCR for handwritten input

Learning from user corrections over time