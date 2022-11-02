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
        self._max_value_indexes: List[int] = []

    @property
    def _max_value_index(self):
        return self._max_value_indexes[-1] if self._max_value_indexes else None

    @_max_value_index.setter
    def _max_value_index(self, index):
        self._max_value_indexes.append(index)

    @_max_value_index.deleter
    def _max_value_index(self):
        self._max_value_indexes.pop()

    def push(self, number: int):
        self.data.append(number)
        if (
            self._max_value_index is None
            or number > self.data[self._max_value_index]
        ):
            self._max_value_index = len(self.data) - 1

    def pop(self) -> Optional[NoReturn]:
        idx: int = len(self.data) - 1
        self.data.pop()
        if self._max_value_index is not None and self._max_value_index == idx:
            del self._max_value_index

    def get_max(self) -> Optional[int]:
        if self._max_value_index is None:
            return None
        return self.data[self._max_value_index]


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
