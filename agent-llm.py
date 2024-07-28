

import ollama
import os
from util import find_phrase, get_google_search_results




#Declare functions, scroll down for code?

ollama.pull("llama3")

modelfile='''
FROM llama3
SYSTEM You are a expert genius online stalker named Agent LLM. You can notice the smallest details that other eyes fail to see. You have a mission, find all information on your subjects. Not talkative
'''

ollama.create(model='Agent-LLM', modelfile=modelfile)




'''

url = "http://example.com"  # Replace with the URL you want to search
phrase = "john doe"
occurrences = find_phrase(url, phrase)

if occurrences:
    print("Found the phrase '{}' on the webpage:".format(phrase))
    for i, occurrence in enumerate(occurrences):
        print("Occurrence {}: {}".format(i+1, occurrence))
else:
    print("The phrase '{}' was not found on the webpage.".format(phrase))

'''


nameDetailed = "Alzuhairi Wheaton IL"
name = "Alzuhairi"

searchFor = ["Al Zuhairi", "Alzuhairi"]


results = get_google_search_results(nameDetailed)


uncompiledData = ""
for result in results:

 
  print(f"Title: {result['title']}")
  print(f"Link: {result['link']}")
  print(f"Snippet: {result['snippet']}")
  print("Soap says:")
  

  uncompiledData += f'''
  Title: {result['title']}'
  Link: {result['link']}
  Snippet: {result['snippet']}
  Term(s) found:
  
  '''

  terms = find_phrase(result['link'], searchFor)
  if terms:
    print("Found the following phrases on the webpage:")
    for phrase, term in terms:
        print(f"Phrase: {phrase}")
        print(f"Occurrence: {term}")
        print("\n")
        uncompiledData += f"Phrase: {phrase}\n"
        uncompiledData += f"Occurrence: {term}\n"
        '''
  else:
    '''
        
    #print("The phrase '{}' was not found on the webpage, sorry!".format(name))
    print("\n")
    '''

    uncompiledData +=f"The phrase '{name}' was not found on the webpage, sorry!\n"
    '''

 





print("###################\n#########")
print(uncompiledData)


f = open(os.path.join('Results/',"UncompiledData.txt"), "w")
f.write(uncompiledData)
f.close()



response = ollama.chat(model='Agent-LLM', messages=[
  {
    'role': 'user',
    'content': 'Analyze, and compile a useful markdown format report with this information. Cite your resources wikipedia style. Make logical connections of relations, locations, education, and all important details. Paragraphs of condensed information, by importance. Information: ' + uncompiledData,
  },
])
print(response['message']['content'])


f = open(os.path.join('Results/',"HenHen.md"), "w")
f.write(response['message']['content'])
f.close()

print("DONE")