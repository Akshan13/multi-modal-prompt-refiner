from pydantic import BaseModel, Field
from typing import List, Optional

class RefinedPrompt(BaseModel):
    """Structured output template for refined prompts."""
    
    intent: str = Field(description="Core product intent/purpose")
    functional_requirements: List[str] = Field(default_factory=List, description="Key Feature needed")
    technical_constraints: List[str] = Field(default_factory=List, description="Budget/material/technology limits")
    expected_deliverables: List[str] = Field(default_factory=List, description="What to produce")
    ambiguities: Optional[List[str]] = Field(default=None, description="Missing or unclear information")
    
    class Config:
        json_schema_extra = {
        "example": {
            "intent": "Design ergonomic wooden chair for office use",
            "functional_requirements": ["Supports up to 100kgs", "4 legs","Armrests"],
            "technical_constraints": ["Made from oak wood", "Cost under $150"],
            "ambiguities": ["Exact dimensions not specified", "Type of finish not mentioned"],
            
        }
        }