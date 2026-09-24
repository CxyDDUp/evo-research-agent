from .base import Tool


class ToolRegistry:

    def __init__(self):
        self.tools = {}


    def register(self, tool: Tool):
        self.tools[tool.name] = tool


    def get(self, name: str) -> Tool:
        return self.tools[name]


    def list_tools(self):
        return list(self.tools.values())