from .models import AgentRequest, AgentResponse
from .message import Message
from .memory import MessageHistory
from .llm.base import LLMClient
from .tools.executor import ToolExecutor


class Agent:

    def __init__(
        self,
        llm: LLMClient,
        tool_executor: ToolExecutor
    ):
        self.llm = llm
        self.tool_executor = tool_executor
        self.history = MessageHistory()


    def run(
        self,
        request: AgentRequest
    ) -> AgentResponse:


        user_message = Message(
            role="user",
            content=request.content
        )

        self.history.add(user_message)


        response = self.llm.generate(
            self.history.get_all()
        )


        if response.tool_calls:

            self.history.add(response)


            for tool_call in response.tool_calls:

                result = self.tool_executor.execute(
                    tool_call.name,
                    **tool_call.arguments
                )


                observation = Message(
                    role="tool",
                    content=str(result)
                )


                self.history.add(observation)


            response = self.llm.generate(
                self.history.get_all()
            )


        self.history.add(response)


        return AgentResponse(
            content=response.content
        )