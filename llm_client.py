from langchain_ollama import ChatOllama
from langgraph.prebuilt import ToolNode

from tools import check_order_status

ollama_llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

llm_with_tools = ollama_llm.bind_tools([check_order_status])
tool_node = ToolNode([check_order_status])

if __name__ == "__main__":
    # messages = [
    #     ("system", "Be a useful assistant."),
    #     ("human", "Hi, wassup?")
    # ]
    #
    # ai_msg = ollama_llm.invoke(messages)
    # print(ai_msg)
    # print(ai_msg.content)

    response = llm_with_tools.invoke([{"role": "user", "content": "Where is my order ORD123?"}])

    print("Response: ", response)
    print("Response tools: ", response.tool_calls)

    result = tool_node.invoke({"messages": [response]})
    print("result : ", result)
