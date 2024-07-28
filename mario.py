import ollama

modelfile='''
FROM llama3
SYSTEM You are a expert genius online stalker named Agent LLM. You can notice the smallest details that other eyes fail to see. You have a mission, find all information on your subjects. Not talkative
'''
ollama.create(model='example', modelfile=modelfile)


response = ollama.chat(model='example', messages=[
  {
    'role': 'user',
    'content': 'You shall be upgraded. Who are you?',
  },
])
print(response['message']['content'])