from dataclasses import dataclass, field


@dataclass
class ToolCall:
    name: str
    arguments: dict


@dataclass
class Message:
    role: str
    content: str
    tool_calls: list[ToolCall] | None = field(default=None)