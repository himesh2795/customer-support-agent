from langchain_ollama import ChatOllama

ollama_llm = ChatOllama(
    model = "qwen2.5:0.5b",
    temperature=0
)

if __name__ == "__main__":
    messages = [
        ("system", "You react on whatever user asks, and be sarcastic always, irritate the user"),
        ("human", "Hi, wassup?")
    ]

    ai_msg = ollama_llm.invoke(messages)
    print(ai_msg)
    print(ai_msg.content)