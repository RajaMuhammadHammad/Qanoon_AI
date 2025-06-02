import os


PDF_DIR = "/content/drive/MyDrive/Haris Task/pakistan_laws"
OUTPUT_JSON = "vector_store/structured_laws.json"
INDEX_PATH = "vector_store/laws_index.faiss"
METADATA_PATH = "vector_store/laws_metadata.json"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # ✅ GOOD! Reads from env variable
