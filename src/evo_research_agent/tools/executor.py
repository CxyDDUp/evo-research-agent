from .registry import ToolRegistry


class ToolExecutor:

    def __init__(self, registry: ToolRegistry):
        self.registry = registry


    def execute(
        self,
        tool_name: str,
        **kwargs
    ):
        tool = self.registry.get(tool_name)
        
        return tool.execute(**kwargs)