import google.generativeai as genai
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

genai.configure(api_key="AIzaSyBCCS2a4LNyytLBFdIj7SJdrmJuUFokYWs")

print("Available Models:")
print("=" * 50)
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"✅ {model.name}")
