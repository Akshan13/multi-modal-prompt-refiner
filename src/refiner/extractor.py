import re 
from refiner.template import RefinedPrompt


def refine_text_to_prompt(raw_text: str) -> RefinedPrompt:
    """Extracts structured prompts from raw text using keywords rules"""
    
    text = raw_text.lower()  # normalize for matching
    
    # Extract intent - FIX: Add opening parenthesis
    intent_match = re.search(r'(design|build|create|develop|make)\s+(.+?)\.', text)
    intent = intent_match.group(0) if intent_match else raw_text.split('.')[0]
    
    # Find Functional Requirements
    requirements = []
    for sentence in raw_text.split('.'):
        if any(word in sentence.lower() for word in ['must', 'should', 'requirement', 'need to', 'shall', 'support', 'require']):
            requirements.append(sentence.strip())
            
    # Find constraints 
    constraints = []
    for sentence in raw_text.split('.'):
        if any(word in sentence.lower() for word in ['budget', 'cost', '$', 'material', 'wood', 'metal', 'timeline', 'deadline']):
            constraints.append(sentence.strip())
    
    # Expected deliverables
    deliverables = []
    if 'cad' in text or '3d model' in text:
        deliverables.append("3D CAD model")
    if 'specification' in text or 'spec' in text:
        deliverables.append("Technical specifications")
    if 'prototype' in text:
        deliverables.append("Physical prototype")
    
    # Ambiguities (flag missing critical info)
    ambiguities = []
    if 'dimension' not in text and 'size' not in text:
        ambiguities.append("Dimensions not specified")
    if not deliverables:
        ambiguities.append("Expected deliverables unclear")
    
    return RefinedPrompt(
        intent=intent.strip(),
        functional_requirements=requirements,
        technical_constraints=constraints,
        expected_deliverables=deliverables,
        ambiguities=ambiguities
    )
