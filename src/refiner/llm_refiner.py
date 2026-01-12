import os
import json 
import warnings
import time
warnings.filterwarnings('ignore', category=FutureWarning)

import google.generativeai as genai  
from refiner.template import RefinedPrompt

# Configure Gemini API
genai.configure(api_key="AIzaSyDgUym-gsw9AxjIc3VevpIZhWKjoMYmIp0")
model = genai.GenerativeModel('models/gemini-2.0-flash-exp')


def refine_with_llm(raw_text: str, max_retries: int = 3) -> RefinedPrompt:
    
    """Using Google Gemini to intelligently extract structured prompts from raw text"""
    
    # Input validation
    if len(raw_text.strip()) < 10:
        raise ValueError("Input text is too short for refinement.")
    
    
    prompt = f"""
You are an expert at analyzing product/project requirements. 
Extract structured information from the following text.

INPUT TEXT:
{raw_text}

OUTPUT FORMAT (JSON):
{{
  "intent": "Main purpose/goal in 1-2 sentences",
  "functional_requirements": ["requirement 1", "requirement 2"],
  "technical_constraints": ["constraint 1", "constraint 2"],
  "expected_deliverables": ["deliverable 1", "deliverable 2"],
  "ambiguities": ["missing info 1", "missing info 2"]
}}

RULES:
1. If no requirements found, use empty list []
2. For ambiguities, list what critical information is missing (dimensions, budget, timeline, etc.)
3. If this is NOT a product/design/project request, set intent to "INVALID_INPUT"
4. Be specific in requirements - extract actual details from text

Return ONLY valid JSON, no extra text or markdown.
"""
    
    # Retry logic
    for attempt in range(max_retries):
        try:
            # Call Gemini API
            response = model.generate_content(prompt)
            result_text = response.text.strip()
            
            # Clean markdown if present
            if result_text.startswith("```json"):
                result_text = result_text.replace("```json", "").replace("```", "").strip()

            # Parse JSON
            data = json.loads(result_text)
            
            # Rejection logic
            if data.get("intent", "").upper() == "INVALID_INPUT":
                raise ValueError("Input Rejected - Not valid product/design request.")
                
            # Create RefinedPrompt instance
            return RefinedPrompt(
                intent=data.get("intent", "Not specified"),
                functional_requirements=data.get("functional_requirements", []),
                technical_constraints=data.get("technical_constraints", []),
                expected_deliverables=data.get("expected_deliverables", []),
                ambiguities=data.get("ambiguities", [])
            )
        
        except json.JSONDecodeError as e:  
            print(f"LLM returned invalid JSON: {result_text}")
            if attempt < max_retries - 1:
                print(f"Retrying... (Attempt {attempt + 2}/{max_retries})")
                time.sleep(5)
            else:
                raise ValueError(f"Failed to parse LLM response as JSON: {e}")
        
        except Exception as e: 
            if "429" in str(e) and attempt < max_retries - 1:
                wait_time = 40
                print(f"Rate limit hit. Waiting {wait_time}s... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
            elif attempt == max_retries - 1:
                print(f"LLM Error after {max_retries} attempts: {e}")
                raise
            else:
                print(f"LLM Error: {e}")
                raise
