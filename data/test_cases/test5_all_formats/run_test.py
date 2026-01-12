import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(project_root, 'src'))

from refiner.multi_modal_refiner import refine_multimodal

print("="*70)
print("TEST 5: All Formats - E-Learning Platform")
print("="*70)

test_dir = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(test_dir, "input.txt")
pdf_path = os.path.join(test_dir, "input.pdf")
docx_path = os.path.join(test_dir, "input.docx")
image_path = os.path.join(test_dir, "input.png")
output_path = os.path.join(test_dir, "output.json")

result = refine_multimodal(
    text_path=text_path,
    pdf_path=pdf_path,
    docx_path=docx_path,
    image_path=image_path
)

with open(output_path, "w") as f:
    f.write(result.model_dump_json(indent=2))

print(f"\n✅ Test 5 Complete!")
print(f"📄 Output saved to: {output_path}")
print("\n" + result.model_dump_json(indent=2))
