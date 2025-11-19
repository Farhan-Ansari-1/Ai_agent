import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
import subprocess
import random

def configure_git(username, email):
    """
    Sets the local Git configuration.
    """
    try:
        subprocess.run(["git", "config", "user.name", username], check=True)
        subprocess.run(["git", "config", "user.email", email], check=True)
        print(f"Git user has been configured as '{username}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error while configuring Git: {e}")
        # This might fail if the configuration is already set, so we continue.
        pass

def generate_blog_post():
    """
    Generates a blog post using the Gemini API.
    """
    print("Starting blog post generation...")
    try:
        model = genai.GenerativeModel('gemini-2.5-pro')
        
        prompt = """
        Write a blog post of about 300 words on a trending topic in AI (Artificial Intelligence) and Cybersecurity.

        The blog post format should be:
        - An attractive title (Example: # AI: The Future of Cybersecurity)
        - Content in simple and engaging language.
        - A conclusion at the end.

        This blog post is for a tech directory website.
        """
        
        response = model.generate_content(prompt)
        print("Blog post generated successfully.")
        return response.text
    except Exception as e:
        print(f"Error while generating the blog post: {e}")
        return None

def save_post_to_file(content):
    """
    Saves the generated content to a markdown file.
    """
    # Assuming your website reads blog posts from the 'content/posts' folder.
    # You can change this path according to your website's structure.
    posts_dir = "content/posts"
    os.makedirs(posts_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    filename = f"{posts_dir}/ai-cybersecurity-update-{timestamp}.md"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Blog post saved to file: {filename}")
        return filename
    except Exception as e:
        print(f"Error while saving the file: {e}")
        return None

def push_to_github(filename, commit_message):
    """
    Pushes the new file to GitHub.
    """
    if not filename:
        print("No filename provided, not pushing to GitHub.")
        return

    try:
        print(f"Pushing '{filename}' to GitHub...")
        subprocess.run(["git", "add", filename], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("File pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running Git command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while pushing to GitHub: {e}")

def main():
    """
    The main function that runs the agent.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found.")
        return

    genai.configure(api_key=api_key)
    
    # Set your GitHub username and email for local testing
    configure_git("Farhan-Ansari-1", "ansarifarhan172006@gmail.com")

    blog_content = generate_blog_post()
    if blog_content:
        saved_filename = save_post_to_file(blog_content)
        commit_msg = f"feat: Add new blog post for {datetime.now().strftime('%Y-%m-%d')}"
        push_to_github(saved_filename, commit_msg)

if __name__ == "__main__":
    main()