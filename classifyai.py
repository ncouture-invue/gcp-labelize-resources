#!/usr/bin/env python3
import os
import openai

import sys
import os

company = sys.argv[1]
if not company:
    print("Usage: {0} <instance name>")
    sys.exit(1)

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Extract the company name from this composite string: {company}",
    temperature=0,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

company = (dict(response)['choices'][0]).to_dict()['text'].strip()
company = ''.join(ch for ch in company if ch.isalnum())
print(f'{company.lower()}')
