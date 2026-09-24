import ast
import operator

from .base import Tool


_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
}


_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _evaluate_node(node):

    if isinstance(node, ast.Expression):
        return _evaluate_node(node.body)

    if isinstance(node, ast.Constant):
        if type(node.value) in (int, float):
            return node.value

        raise ValueError(
            "Only numbers are allowed."
        )

    if isinstance(node, ast.BinOp):

        operator_type = type(node.op)

        if operator_type not in _BINARY_OPERATORS:
            raise ValueError(
                "Unsupported operator."
            )

        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)

        operation = _BINARY_OPERATORS[
            operator_type
        ]

        return operation(
            left,
            right
        )

    if isinstance(node, ast.UnaryOp):

        operator_type = type(node.op)

        if operator_type not in _UNARY_OPERATORS:
            raise ValueError(
                "Unsupported unary operator."
            )

        operand = _evaluate_node(
            node.operand
        )

        operation = _UNARY_OPERATORS[
            operator_type
        ]

        return operation(
            operand
        )

    raise ValueError(
        "Unsupported expression."
    )


class CalculatorTool(Tool):

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return "Calculate mathematical expressions."

    def execute(
        self,
        expression: str
    ):

        tree = ast.parse(
            expression,
            mode="eval"
        )

        return _evaluate_node(
            tree
        )