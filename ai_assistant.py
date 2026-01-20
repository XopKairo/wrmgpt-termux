# ai_assistant.py

import openai
import os
import subprocess
import sys
import time

# Set your OpenAI API key
openai.api_key = os.getenv("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")

def fix_errors(code):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Fix the errors in the following code:\n\n{code}\n\nCorrected code:",
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def answer_question(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer the following question:\n\n{question}\n\nAnswer:",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def generate_code(description):
    response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=f"Generate Python code for the following description:\n\n{description}\n\nCode:",
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def generate_command(description):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a shell command for the following description:\n\n{description}\n\nCommand:",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def monitor_termux():
    while True:
        command = input("Termux $ ")
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            print("AI Assistant: Let me try to fix that for you.")
            fix_command = generate_command(f"Fix the error in the following command: {command}")
            print(f"AI Assistant: Try this command instead: {fix_command}")
            try:
                result = subprocess.run(fix_command, shell=True, check=True, capture_output=True, text=True)
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"AI Assistant: I'm sorry, I couldn't fix the issue. Here's the error: {e}")

        time.sleep(1)

if __name__ == "__main__":
    monitor_termux()
