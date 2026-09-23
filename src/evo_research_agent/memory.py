from .message import Message


class MessageHistory:

    def __init__(self):
        self.messages: list[Message] = []


    def add(self, message: Message):
        self.messages.append(message)


    def get_all(self) -> list[Message]:
        return self.messages