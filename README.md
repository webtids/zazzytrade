# zazzytrade

zazzytrade-project

## ChatGPT API Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and replace the placeholder with your OpenAI API key:
   ```bash
   cp .env.example .env
   # edit .env and set OPENAI_API_KEY
   ```
3. Run the example script to verify your key:
   ```bash
   python chatgpt_example.py
   ```
   If the key is missing, the script will prompt you to add it.

## Web UI

1. Start the Flask app:
   ```bash
   python app.py
   ```
2. Open `http://localhost:5000` in a browser to use the mobile‑friendly chat interface.
