# 69117778
# Сначала создадим приоритетную очередь(бинарную невозрастающую кучу max-heap).
# Вставим в неё по одному все входящие элементы, сохраняя свойства кучи.
# Так как нам нужна сортировка от большего к меньшему, на вершине пирамиды
# должен оказаться самый большой элемент. При вставке нового узла,
# добавляем его в конец кучи(в конец массива), и производим проверку, если он
# больше чем родительский, то меняем местами("просеивание вверх").
# После того как куча была создана, необходимо в цикле забирать самый
# приоритетный элемент и удалять его из кучи, а на место извлечённого элемента,
# подставлять последний элемент из кучи и производить "просеивание вниз".
# Временная сложность: O(nlog(n))
# Пространственная сложность: O(1)

import sys
from dataclasses import dataclass
from typing import (
    List,
    Any,
)


@dataclass
class Participant:
    login: str
    resolved_tasks: int
    fine: int

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Participant):
            raise AssertionError("Incorrect type for comparison")
        if self.resolved_tasks == other.resolved_tasks:
            if self.fine == other.fine:
                return self.login > other.login
            return self.fine > other.fine
        return self.resolved_tasks < other.resolved_tasks

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, Participant):
            raise AssertionError("Incorrect type for comparison")
        return not self < other


class ParticipantHeap:
    def __init__(self) -> None:
        self._data: List[Participant] = [
            Participant(login="", resolved_tasks=0, fine=0),
        ]

    def add(self, participant: Participant) -> None:
        self._data.append(participant)
        self._sift_up(idx=self.size - 1)
        return None

    def pop(self) -> Participant:
        result: Participant = self._data[1]
        self._data[1] = self._data[-1]
        del self._data[-1]
        self._sift_down(1)
        return result

    @property
    def size(self) -> int:
        return len(self._data)

    def _sift_down(self, idx: int) -> None:
        left: int = 2 * idx
        right: int = 2 * idx + 1
        size: int = self.size - 1
        if left > size:
            return None
        if (right <= size) and (self._data[left] < self._data[right]):
            index_largest: int = right
        else:
            index_largest = left
        if self._data[idx] < self._data[index_largest]:
            self._data[idx], self._data[index_largest] = (
                self._data[index_largest],
                self._data[idx],
            )
            return self._sift_down(index_largest)
        return None

    def _sift_up(self, idx: int) -> None:
        if idx == 1:
            return None
        parent_index: int = idx // 2
        if self._data[parent_index] < self._data[idx]:
            self._data[idx], self._data[parent_index] = (
                self._data[parent_index],
                self._data[idx],
            )
            self._sift_up(parent_index)
        return None


def get_data() -> List[List[str]]:
    length: int = int(input())
    participants: List[List[str]] = []
    for _ in range(length):
        participants.append(sys.stdin.readline().rstrip().split())
    return participants


def main() -> None:
    participants: List[List[str]] = get_data()
    heap: ParticipantHeap = ParticipantHeap()
    for i in participants:
        participant: Participant = Participant(
            login=i[0],
            resolved_tasks=int(i[1]),
            fine=int(i[2]),
        )
        heap.add(participant)
    while heap.size > 1:
        print(heap.pop().login)


if __name__ == "__main__":
    main()
