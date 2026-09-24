from .base import LLMClient

from ..message import Message, ToolCall


class MockLLM(LLMClient):

    def generate(
        self,
        messages: list[Message]
    ) -> Message:

        last_message = messages[-1]


        # Tool execution result
        if last_message.role == "tool":

            return Message(
                role="assistant",
                content=f"The calculation result is {last_message.content}"
            )


        # Decide whether to use tool
        if "calculate" in last_message.content.lower():

            return Message(
                role="assistant",
                content="",
                tool_calls=[
                    ToolCall(
                        name="calculator",
                        arguments={
                            "expression": "100+200"
                        }
                    )
                ]
            )


        return Message(
            role="assistant",
            content="Mock response"
        )