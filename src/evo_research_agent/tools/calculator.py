from .base import Tool


class CalculatorTool(Tool):

    @property
    def name(self) -> str:
        return "calculator"


    @property
    def description(self) -> str:
        return "Calculate mathematical expressions."


    def execute(self, expression: str):
        return eval(expression)