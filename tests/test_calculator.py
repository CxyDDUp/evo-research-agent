from evo_research_agent.tools.calculator import CalculatorTool


tool = CalculatorTool()


print(tool.name)

print(tool.description)

print(tool.execute("1 + 2 * 3"))