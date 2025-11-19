# AI Content Agent for Automated Blogging

This project is an AI-powered agent that automatically generates and publishes blog posts on topics related to Artificial Intelligence and Cybersecurity. It uses Google's Gemini API for content creation and automates the process of pushing new articles to a GitHub repository, making it ideal for powering a static site blog (like Hugo, Jekyll, etc.).

## ✨ Features

- **Automated Content Creation**: Generates unique blog posts using the Gemini API.
- **Dynamic Topics**: Randomly selects from a predefined list of AI and Cybersecurity topics for fresh content every time.
- **Markdown Format**: Saves articles in a clean, blog-ready Markdown format.
- **Git Automation**: Automatically adds, commits, and pushes the new blog post to the GitHub repository.

## ⚙️ How It Works

1.  **Topic Selection**: The script randomly picks a topic from a predefined list (e.g., "The future of Ethical Hacking", "AI in threat detection").
2.  **Content Generation**: It sends a dynamic prompt with the chosen topic to the Gemini API to generate a ~300-word article.
3.  **File Creation**: The generated content is saved into a new Markdown file inside the `content/posts/` directory. The filename includes a timestamp to ensure it's unique.
4.  **Git Push**: The script then executes Git commands to stage the new file, commit it with a descriptive message, and push it to the `main` branch of the repository.

## 🚀 Local Setup and Usage

Follow these steps to run the agent on your local machine.

### 1. Prerequisites
- Python 3.8+
- Git installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/Farhan-Ansari-1/Ai_agent.git
cd Ai_agent
```

### 3. Set Up Virtual Environment
Create and activate a Python virtual environment.
```bash
# For Windows
python -m venv .venv
.venv\Scripts\activate

# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
Install the required Python packages.
```bash
pip install google-generativeai python-dotenv
```

### 5. Create `.env` File
Create a `.env` file in the root of the project and add your Gemini API key.
```
GEMINI_API_KEY="your_actual_api_key_here"
```
> **Note**: The `.gitignore` file is already configured to prevent this file from being pushed to GitHub.

### 6. Run the Agent
Execute the script to generate and publish a new blog post.
```bash
python scripts/blog_agent.py
```

## ⏭️ Next Steps

The next goal is to fully automate this process using **GitHub Actions**, allowing the agent to run on a schedule (e.g., daily) without any manual intervention.
