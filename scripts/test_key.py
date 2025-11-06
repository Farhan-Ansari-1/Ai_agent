# scripts/test_key.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()   # loads .env from repo root
KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
print("Using KEY from env?:", bool(KEY))

if not KEY:
    raise SystemExit("No key in env (GEMINI_API_KEY or GOOGLE_API_KEY)")

# Configure SDK
genai.configure(api_key=KEY)

# Try list models (SDK method)
try:
    models = list(genai.list_models())
    print("Models available (first 10):")
    for m in models[:10]:
        # The model object `m` has a 'name' attribute.
        # We can use getattr for safe access. If it's missing for any reason,
        # we'll fall back to converting the object to a string.
        model_name = getattr(m, "name", str(m))
        print(f" - {model_name}")
except Exception as e:
    print("ERROR while listing models:", repr(e))
    raise
