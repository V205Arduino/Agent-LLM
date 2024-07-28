import ollama
import os

ollama.pull("llama3")

modelfile='''
FROM llama3
SYSTEM You are a expert genius online named Agent LLM. You can notice the smallest details that other eyes fail to see. You have a mission, find all information on your subjects. 
'''

ollama.create(model='Agent-LLM', modelfile=modelfile)





f = open(os.path.join('Results/',"HenHen.md"), "r")

redact=f.read()
f.close()
response = ollama.chat(model='Agent-LLM', messages=[
  {
    'role': 'user',
    'content': 'Redact mode, redact all PII from the provided data, and all URLs that contain PII. REMEMBER URLS. Here is the content to be redacted: ' + redact,
  },
])
print(response['message']['content'])


f = open(os.path.join('Results/',"Redacted.md"), "w")
f.write(response['message']['content'])
f.close()
