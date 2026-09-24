from evo_research_agent.tools.base import Tool


class DemoTool(Tool):

    @property
    def name(self):
        return "demo"


    @property
    def description(self):
        return "A demo tool"


    def execute(self, value):
        return value


tool = DemoTool()


print(tool.name)

print(tool.description)

print(tool.execute("hello"))