from .base import LLMClient

from ..message import Message, ToolCall


class MockLLM(LLMClient):

    def generate(
        self,
        messages: list[Message]
    ) -> Message:

        last_message = messages[-1]

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