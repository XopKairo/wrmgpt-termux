#!/bin/sh

# Navigate to the script directory
cd "$(dirname "$0")"

# Set any necessary environment variables
export PYTHONPATH="."
export OPENAI_API_KEY=$(cat /path/to/your/secret/file)

# Install required Python packages
pip install openai

# Run the Python script
python ai_assistant.py
