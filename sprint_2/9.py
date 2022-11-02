import enum
import sys
from typing import (
    List,
    Optional,
    Tuple,
    NoReturn,
)


class MyQueueSized:
    def __init__(self, max_size: int):
        self.data: List[Optional[int]] = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x: int):
        if self.size == self.max_size:
            raise AssertionError("Max size")
        self.data[self.tail] = x
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop(self) -> Optional[NoReturn]:
        if self.is_empty():
            return None
        x = self.data[self.head]
        self.data[self.head] = None
        self.size -= 1
        self.head = (self.head + 1) % self.max_size
        return x

    def peek(self):
        return self.data[self.head]


def get_commands(command_length: int) -> List[Tuple[str, Optional[int]]]:
    commands: List[Tuple[str, int]] = []
    for _ in range(command_length):
        data: List[str, Optional[str]] = (
            sys.stdin.readline().rstrip().split(" ")
        )
        command: Tuple[str, Optional[int]] = (
            data[0],
            int(data[1]) if len(data) > 1 else None,
        )
        commands.append(command)
    return commands


class CommandFuncName(enum.Enum):
    peek = "peek"
    push = "push"
    pop = "pop"
    size = "size"


def execute_command(stack: MyQueueSized, command: Tuple[str, Optional[int]]):
    func = command[0]
    number: Optional[int] = command[1]
    if func == CommandFuncName.peek.value:
        print(stack.peek())
    elif func == CommandFuncName.push.value:
        try:
            stack.push(number)
        except AssertionError:
            print("error")
    elif func == CommandFuncName.pop.value:
        print(stack.pop())
    elif func == CommandFuncName.size.value:
        print(stack.size)


def main():
    commands_length: int = int(input())
    max_size: int = int(input())
    stack = MyQueueSized(max_size=max_size)
    for command in get_commands(commands_length):
        execute_command(stack, command)


main()
