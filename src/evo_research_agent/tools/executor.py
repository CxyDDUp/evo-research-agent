from .registry import ToolRegistry
from .result import ToolResult


class ToolExecutor:

    def __init__(
        self,
        registry: ToolRegistry
    ):
        self.registry = registry


    def execute(
        self,
        tool_name: str,
        **kwargs
    ) -> ToolResult:

        try:

            tool = self.registry.get(
                tool_name
            )

            result = tool.execute(
                **kwargs
            )


            return ToolResult(
                success=True,
                output=str(result)
            )


        except Exception as e:

            return ToolResult(
                success=False,
                output="",
                error=str(e)
            )