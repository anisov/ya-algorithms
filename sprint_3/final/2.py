# 68459084
# Сортировка происходит с использованием метода двух указателей с определённой
# логикой смещения, кроме того используется рекурсия для дробления массива на
# части. Для данной реализации нужно выбрать опорный элемент, а затем выполнить
# сортировку, так что бы элементы, которые больше опорного элемента, были
# справа, а те что меньше слева (в нашем случае, наоборот, участник с лучшим
# решением должен быть слева, а с худшим справа), для сравнения участников,
# используется функция comparator. А для реализации смещения указателей и
# перестановки элементов, использовался подход при котором левый указатель
# будет смещаться до тех пор, пока он не будет указывать на элемент больше
# опорного, затем таким же способом необходимо смещать правый указатель,
# пока он не будет указывать на элемент, меньше опорного,
# после того как эти два элемента будут найдены, нужно их переставить.
# Опорный элемент будет находиться рандомно(для оптимизации сортировки
# отсортированного массива), так же можно было бы всегда брать первый элемент
# как опорный, экономя производительность на получение рандомного элемента.
# Временная сложность 0(n*log(n)). Худший случай O(n^2).
# Пространственная сложность O(1). Требуется дополнительная память для хранения
# стека вызовов.

import sys
from abc import (
    abstractmethod,
    ABC,
)
from dataclasses import dataclass
from random import randint
from typing import (
    List,
    Optional,
    Callable,
    TypeVar,
    Generic,
    Tuple,
    Any,
)


class Comparable(ABC):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        ...

    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        ...


Item = TypeVar("Item", bound=Comparable)


class InPlaceQuickSort(Generic[Item]):
    __slots__ = ()

    @staticmethod
    def _compare_items(
        first: Item,
        second: Item,
        comparator: Optional[Callable[[Item, Item], bool]],
    ) -> bool:
        if comparator:
            return comparator(first, second)
        return first > second

    @classmethod
    def _partition(
        cls,
        array: List[Item],
        low: int,
        high: int,
        comparator: Optional[Callable[[Item, Item], bool]] = None,
    ) -> Tuple[int, int]:
        pivot: Item = array[randint(low, high)]
        while low <= high:
            while low <= high and cls._compare_items(
                first=array[high], second=pivot, comparator=comparator
            ):
                high -= 1
            while low <= high and cls._compare_items(
                first=pivot, second=array[low], comparator=comparator
            ):
                low += 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
                low += 1
                high -= 1
        return low, high

    @classmethod
    def sort(
        cls,
        array: List[Item],
        comparator: Optional[Callable[[Item, Item], bool]] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> None:
        if start is None:
            start = 0
        if end is None:
            end = len(array) - 1
        if start >= end:
            return
        low, high = cls._partition(array, start, end, comparator)
        cls.sort(array, comparator, start, high)
        cls.sort(array, comparator, low, end)


@dataclass
class Participant(Comparable):
    name: str
    solved_task_count: int
    fine: int

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, Participant):
            raise AssertionError("Incorrect type for comparison")
        if (
            self.solved_task_count == other.solved_task_count
            and self.fine == other.fine
        ):
            return self.name > other.name
        if self.solved_task_count == other.solved_task_count:
            return self.fine > other.fine
        return self.solved_task_count < other.solved_task_count

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Participant):
            raise AssertionError("Incorrect type for comparison")
        return other > self


def get_data() -> List[Participant]:
    length: int = int(input())
    result: List[Participant] = []
    for _ in range(length):
        data: List[str] = sys.stdin.readline().rstrip().split()
        result.append(
            Participant(
                name=data[0], solved_task_count=int(data[1]), fine=int(data[2])
            )
        )
    return result


def main() -> None:
    data: List[Participant] = get_data()
    InPlaceQuickSort[Participant].sort(array=data)
    for i in data:
        print(i.name)


if __name__ == "__main__":
    main()
