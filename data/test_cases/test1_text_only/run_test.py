import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(project_root, 'src'))

from refiner.multi_modal_refiner import refine_multimodal
import json

print("="*70)
print("TEST 1: Text Only - Real Estate CRM System")
print("="*70)

# Get current directory
test_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(test_dir, "input.txt")
output_path = os.path.join(test_dir, "output.json")

# Run refinement
result = refine_multimodal(text_path=input_path)

# Save output
with open(output_path, "w") as f:
    f.write(result.model_dump_json(indent=2))

print(f"\nTest 1 Complete!")
print(f"Output saved to: {output_path}")
print("\n" + result.model_dump_json(indent=2))
