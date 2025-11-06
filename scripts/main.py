import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
import sys


def main():
    """
    Main function to initialize the model and generate content.
    """
    load_dotenv()  # Load environment variables from .env
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise SystemExit("No API key found in environment variables.")

    genai.configure(api_key=api_key)

    # Initialize the generative model
    # Using a model available to your API key, like gemini-2.5-pro
    model = genai.GenerativeModel('gemini-2.5-pro')

    # --- Auto-saving functionality ---
    # Create a unique filename with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"chat_log_{timestamp}.txt"
    print(f"Conversation will be saved to: {log_filename}")
    # --- End of auto-saving setup ---

    print("Connected to model. You can start chatting now (type 'quit' or 'exit' to end).")

    while True:
        try:
            prompt = input("You: ")

            if prompt.lower() in ["quit", "exit"]:
                print("Exiting chat. Goodbye!")
                break

            response = model.generate_content(prompt)
            print(f"AI: {response.text}")

            # Auto-save the conversation to the log file
            with open(log_filename, 'a', encoding='utf-8') as f:
                f.write(f"You: {prompt}\n")
                f.write(f"AI: {response.text}\n\n")

        except (KeyboardInterrupt, EOFError):
            print("\nExiting chat. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
