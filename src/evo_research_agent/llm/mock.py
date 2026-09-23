from .base import LLMClient

from ..message import Message, Role


class MockLLM(LLMClient):

    def generate(
        self,
        messages: list[Message]
    ) -> Message:

        last_message = messages[-1]

        return Message(
            role=Role.ASSISTANT,
            content=f"Mock response to: {last_message.content}"
        )   