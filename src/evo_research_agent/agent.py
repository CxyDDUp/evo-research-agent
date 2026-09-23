from .models import AgentRequest, AgentResponse
from .message import Message, Role
from .memory import MessageHistory


class Agent:

    def __init__(self):
        self.history = MessageHistory()


    def run(self, request: AgentRequest) -> AgentResponse:

        user_message = Message(
            role=Role.USER,
            content=request.content
        )

        self.history.add(user_message)


        response = Message(
            role=Role.ASSISTANT,
            content=f"You said: {request.content}"
        )

        self.history.add(response)


        return AgentResponse(
            content=response.content
        )