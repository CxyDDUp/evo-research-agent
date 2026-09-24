from .base import LLMClient

from ..message import Message, ToolCall


class MockLLM(LLMClient):

    def generate(
        self,
        messages: list[Message]
    ) -> Message:

        last_message = messages[-1]


        # 1. Receive tool observation
        if last_message.role == "tool":

            if last_message.content.startswith(
                "Tool error:"
            ):

                error_message = (
                    last_message.content
                    .removeprefix("Tool error:")
                    .strip()
                )

                return Message(
                    role="assistant",
                    content=(
                        f"Calculation failed: "
                        f"{error_message}"
                    )
                )

            return Message(
                role="assistant",
                content=(
                    f"The calculation result is "
                    f"{last_message.content}"
                )
            )


        # 2. Decide whether to call calculator
        user_content = (
            last_message.content.strip()
        )


        if user_content.lower().startswith(
            "calculate"
        ):

            expression = user_content[
                len("calculate"):
            ].strip()


            if not expression:

                return Message(
                    role="assistant",
                    content=(
                        "Please provide an expression "
                        "after 'calculate'."
                    )
                )


            return Message(
                role="assistant",
                content="",
                tool_calls=[
                    ToolCall(
                        name="calculator",
                        arguments={
                            "expression": expression
                        }
                    )
                ]
            )


        # 3. Normal response
        return Message(
            role="assistant",
            content="Mock response"
        )