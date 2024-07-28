import ollama
import os

ollama.pull("llama3")

modelfile='''
FROM llama3
SYSTEM You are Agent-LLM, you must redact all sensitive information such as first, middle, last names, sensitive URLs, locations, and everything you think could risk the subject. 
'''

ollama.create(model='Agent-LLM-Redact', modelfile=modelfile)





f = open(os.path.join('Results/',"HenHen.md"), "r")

redact=f.read()
f.close()
response = ollama.chat(model='Agent-LLM-Redact', messages=[
  {
    'role': 'user',
    'content': 'REDACT FIRST AND LAST NAMES, LOCATIONS, SCHOOLS, GENDERS, CONTACT INFORMATION, URLS. REDACT: ' + redact,
  },
])
print(response['message']['content'])


f = open(os.path.join('Results/',"Redacted.md"), "w")
f.write(response['message']['content'])
f.close()
