# 67983501
# Для решения данной задачи использовался двусвязный список, так как это
# решение более оптимиально, нежели решение с использованием списка. Это
# связанно с тем, что список в python представляет собой массив с указателями
# на объекты в памяти, в языке С это не так, там при получении элемента по
# индексу происходит сдвиг в той же области памяти, где находится массив, по
# этому, там оптимальнее использовать массив, это быстрее. Так же, список в
# Python предполагает два действия: 1) сначала через индекс получить ссылку на
# объект 2) а затем получить сам объект уже по ссылке, что приводит к лишним
# операциям.
# Помимо этого, решение через двусвязный список может потреблять меньше памяти,
# так как не создаётся большой массив в памяти со ссылками на значения.
# Конечно, в Python есть оптимизации, и все значение в массиве, при
# инициализации, буду ссылаться на один и тот же объект в памяти(допустим
# None), что не приведёт к большим лишним расходам, но всё равно, сам массив
# со ссылками на один и тот же объект будет существовать, несмотря на то, что
# сама структура может и не предполагает хранить столько значений(когда у нас
# задано большое значение max_size, а данных передаётся в наш дек значительно
# меньше).
# Можно возразить, что сами объекты Node потребляют много лишней памяти. Но для
# лучшей оптимизации, я использовал __slots__. А так как в Python всё является
# объектом(структурой в С), что int, что str, то даже эти элементарные типы
# так же имеют накладные расходы и занимают гораздо больше памяти, чем просто
# типы данных в С.
# Поэтому, разница в потребление памяти между объектом класса Node и просто
# числом не столь велика, ведь всё является большой структурой С(объектом в
# терминологии Python). По этому, исходя из этих рассуждений, я реализовал
# алгоритм данным способом, что показало хороший результат 0.688s 20.42Mb.
# Временная сложность: 0(1)
# Пространственная сложность: 0(n)

import sys
from typing import (
    List,
    Optional,
    Tuple,
    Dict,
    Callable,
)


class DeqLinkedListError(BaseException):
    pass


class DeqLinkedList:
    __slots__ = ("head", "tail", "max_size", "size")

    class Node:
        __slots__ = ("value", "next_item", "prev_item")

        def __init__(
            self,
            value: int,
            next_item: Optional["DeqLinkedList.Node"] = None,
            prev_item: Optional["DeqLinkedList.Node"] = None,
        ) -> None:
            self.value: int = value
            self.next_item: Optional[DeqLinkedList.Node] = next_item
            self.prev_item: Optional[DeqLinkedList.Node] = prev_item

    def __init__(self, max_size: int) -> None:
        self.head: Optional[DeqLinkedList.Node] = None
        self.tail: Optional[DeqLinkedList.Node] = None
        self.max_size: int = max_size
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def _push_validate(self) -> None:
        if self.size == self.max_size:
            raise DeqLinkedListError("Maximum size reached")

    def _pop_validate(self) -> None:
        if self.is_empty():
            raise DeqLinkedListError("No elements")

    def _init_list(self, value: int) -> None:
        self.head = self.Node(value=value)
        self.tail = self.head

    def _push(self, value: int, front=True) -> None:
        self._push_validate()
        self.size += 1
        if self.head is None:
            self._init_list(value=value)
            return
        if front:
            node = self.Node(value=value, next_item=self.head)
            self.head.prev_item = node
            self.head = node
            return
        node = self.Node(value=value, prev_item=self.tail)
        self.tail.next_item = node
        self.tail = node

    def push_back(self, value: int) -> None:
        self._push(value=value, front=False)

    def push_front(self, value: int) -> None:
        self._push(value=value, front=True)

    def _pop(self, node: "DeqLinkedList.Node") -> int:
        self._pop_validate()
        self.size -= 1
        value: int = node.value
        if node.next_item and node.prev_item is None:
            self.head = node.next_item
            self.head.prev_item = None
            return value
        if node.prev_item and node.next_item is None:
            self.tail = node.prev_item
            self.tail.next_item = None
            return value
        self.head = None
        self.tail = None
        return value

    def pop_front(self) -> int:
        return self._pop(self.head)

    def pop_back(self) -> int:
        return self._pop(self.tail)


def get_commands(command_length: int) -> List[Tuple[str, Optional[int]]]:
    commands: List[Tuple[str, int]] = []
    for _ in range(command_length):
        data: List[str, Optional[str]] = sys.stdin.readline().rstrip().split()
        command: Tuple[str, Optional[int]] = (
            data[0],
            int(data[1]) if len(data) > 1 else None,
        )
        commands.append(command)
    return commands


class DeqCommand:
    push_back: str = "push_back"
    push_front: str = "push_front"
    pop_front: str = "pop_front"
    pop_back: str = "pop_back"

    def __init__(
        self, stack: DeqLinkedList, func: str, value: Optional[int] = None
    ):
        self.stack: DeqLinkedList = stack
        self.func: str = func
        self.value: int = value

    def execute(self) -> Optional[int]:
        action: Dict[str, Callable] = {
            self.push_back: self.stack.push_back,
            self.push_front: self.stack.push_front,
            self.pop_front: self.stack.pop_front,
            self.pop_back: self.stack.pop_back,
        }
        if self.func in {self.push_back, self.push_front}:
            return action[self.func](value=self.value)
        return action[self.func]()


def execute_command(stack: DeqLinkedList, command: Tuple[str, Optional[int]]):
    func: str = command[0]
    value: Optional[int] = command[1]
    try:
        value = DeqCommand(stack=stack, func=func, value=value).execute()
        if value is not None:
            print(value)
    except DeqLinkedListError:
        print("error")


def main():
    commands_length: int = int(input())
    max_size: int = int(input())
    stack: DeqLinkedList = DeqLinkedList(max_size=max_size)
    for command in get_commands(commands_length):
        execute_command(stack, command)


if __name__ == "__main__":
    main()
