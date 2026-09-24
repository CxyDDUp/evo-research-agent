from evo_research_agent.tools.registry import ToolRegistry
from evo_research_agent.tools.calculator import CalculatorTool
from evo_research_agent.tools.executor import ToolExecutor


registry = ToolRegistry()


registry.register(
    CalculatorTool()
)


executor = ToolExecutor(
    registry
)


result = executor.execute(
    "calculator",
    expression="100 * 20"
)


print(result)

print(result.success)

print(result.output)