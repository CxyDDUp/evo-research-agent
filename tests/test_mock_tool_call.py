from evo_research_agent.llm.mock import MockLLM
from evo_research_agent.message import Message


llm = MockLLM()


messages = [
    Message(
        role="user",
        content="calculate something"
    )
]


response = llm.generate(messages)


print(response)

print(response.tool_calls)