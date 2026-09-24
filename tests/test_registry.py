from evo_research_agent.tools.registry import ToolRegistry
from evo_research_agent.tools.calculator import CalculatorTool


registry = ToolRegistry()


calculator = CalculatorTool()


registry.register(calculator)


tool = registry.get("calculator")


print(tool.name)

print(tool.execute("10 * 20"))


print(
    [t.name for t in registry.list_tools()]
)