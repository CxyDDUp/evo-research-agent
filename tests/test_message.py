from evo_research_agent.message import Message, ToolCall


tool_call = ToolCall(
    name="calculator",
    arguments={
        "expression": "100+200"
    }
)


message = Message(
    role="assistant",
    content="",
    tool_calls=[
        tool_call
    ]
)


print(message)

print(message.tool_calls[0].name)

print(message.tool_calls[0].arguments)