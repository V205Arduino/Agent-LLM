import ollama

while True:

    userInput = input("\nEnter your message to the LLM: ")

    stream = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': userInput}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
    print("Done, ready for next message")
