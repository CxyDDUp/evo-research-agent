from .models import AgentRequest, AgentResponse
from .message import Message
from .memory import MessageHistory
from .llm.base import LLMClient


class Agent:

    def __init__(
        self,
        llm: LLMClient
    ):
        self.llm = llm
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
        # if response.tool_calls:

        #     execute tools

        #     add observation

        #     call llm again
        # else:
        #     return response

        self.history.add(response)


        return AgentResponse(
            content=response.content
        )