from .agent import Agent
from .models import AgentRequest
from .llm.mock import MockLLM


def main():

    agent = Agent(
        llm=MockLLM()
    )

    user_input = input("You> ")

    request = AgentRequest(
        content=user_input
    )

    response = agent.run(request)

    print(
        f"Agent> {response.content}"
    )


if __name__ == "__main__":
    main()