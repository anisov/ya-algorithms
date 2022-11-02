import enum
import sys
from typing import (
    List,
    Optional,
    Tuple,
    NoReturn,
)


class StackMax:
    def __init__(self):
        self.data: List[int] = []

    def push(self, x: int):
        self.data.append(x)

    def pop(self) -> Optional[NoReturn]:
        self.data.pop()

    def get_max(self) -> Optional[int]:
        if not self.data:
            return None
        return max(self.data)


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
    get_max = "get_max"
    push = "push"
    pop = "pop"


def execute_command(stack: StackMax, command: Tuple[str, Optional[int]]):
    func = command[0]
    number: Optional[int] = command[1]
    if func == CommandFuncName.get_max.value:
        print(stack.get_max())
    elif func == CommandFuncName.push.value:
        stack.push(number)
    elif func == CommandFuncName.pop.value:
        try:
            stack.pop()
        except IndexError:
            print("error")


def main():
    stack = StackMax()
    length: int = int(input())
    for command in get_commands(length):
        execute_command(stack, command)


main()
