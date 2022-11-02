import enum
import sys
from typing import (
    List,
    Optional,
    Tuple,
    NoReturn,
    Union,
)


class MyQueue:
    class Node:
        def __init__(self, value, next_item=None, prev_item=None) -> None:
            self.value = value
            self.next_item = next_item
            self.prev_item = prev_item

    def __init__(self) -> None:
        self.head: Optional[MyQueue.Node] = None
        self.tail: Optional[MyQueue.Node] = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def put(self, x: int) -> None:
        if self.head is None:
            self.head = self.Node(value=x)
            self.tail = self.head
        else:
            node = self.Node(value=x, prev_item=self.tail)
            self.tail.next_item = node
            self.tail = node
        self.size += 1

    def get(self) -> Union[NoReturn, int]:
        if not self.size:
            raise AssertionError("No elements")
        value: int = self.head.value
        if self.head.next_item:
            self.head = self.head.next_item
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return value


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
    put = "put"
    get = "get"
    size = "size"


def execute_command(stack: MyQueue, command: Tuple[str, Optional[int]]):
    func = command[0]
    number: Optional[int] = command[1]
    if func == CommandFuncName.put.value:
        stack.put(number)
    elif func == CommandFuncName.get.value:
        try:
            print(stack.get())
        except AssertionError:
            print("error")
    elif func == CommandFuncName.size.value:
        print(stack.size)


def main():
    commands_length: int = int(input())
    stack = MyQueue()
    for command in get_commands(commands_length):
        execute_command(stack, command)


main()
