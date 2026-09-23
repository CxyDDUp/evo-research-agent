from .models import AgentRequest, AgentResponse


from .models import AgentRequest, AgentResponse


class Agent:
    def run(self, request: AgentRequest) -> AgentResponse:
        return AgentResponse(
            content=f"You said: {request.content}"
        )