def render_result(result):
    print("\n========== EXECUTION TRACE ==========")

    for message in result["messages"]:
        if message.type == "human":
            print(f"\n👤 User:\n{message.content}")

        elif message.type == "ai":
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    print(
                        f"\n🤖 Agent decided to use tool:\n"
                        f"   Tool: {tool_call['name']}\n"
                        f"   Args: {tool_call['args']}"
                    )
            elif message.content:
                print(f"\n🤖 Agent:\n{message.content}")

        elif message.type == "tool":
            print(
                f"\n🔧 Tool Result:\n"
                f"   {message.name}: {message.content}"
            )

    print("\n=====================================")