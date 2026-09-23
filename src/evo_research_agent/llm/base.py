from abc import ABC, abstractmethod

from ..message import Message


class LLMClient(ABC):

    @abstractmethod
    def generate(
        self,
        messages: list[Message]
    ) -> Message:
        pass