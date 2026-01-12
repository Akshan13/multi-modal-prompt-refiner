import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(project_root, 'src'))

from refiner.multi_modal_refiner import refine_multimodal

print("="*70)
print("TEST 2: PDF Only - Drone Delivery System")
print("="*70)

test_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(test_dir, "input.pdf")
output_path = os.path.join(test_dir, "output.json")

result = refine_multimodal(pdf_path=input_path)

with open(output_path, "w") as f:
    f.write(result.model_dump_json(indent=2))

print(f"\nTest 2 Complete!")
print(f"Output saved to: {output_path}")
print("\n" + result.model_dump_json(indent=2))
