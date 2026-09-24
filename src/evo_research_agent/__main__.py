from .agent import Agent
from .models import AgentRequest

from .llm.mock import MockLLM

from .tools.registry import ToolRegistry
from .tools.calculator import CalculatorTool
from .tools.executor import ToolExecutor


def main():

    registry = ToolRegistry()

    registry.register(
        CalculatorTool()
    )


    tool_executor = ToolExecutor(
        registry
    )


    agent = Agent(
        llm=MockLLM(),
        tool_executor=tool_executor
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