#!/bin/sh

# Navigate to the script directory
cd "$(dirname "$0")"

# Set any necessary environment variables
export PYTHONPATH="."
export OPENAI_API_KEY="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"

# Install required Python packages
pip install openai

# Run the Python script
python ai_assistant.py
