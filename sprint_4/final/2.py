"""
# 68663738
Для решения данной задачи использовался метод открытой адресации. В качестве
метода пробирования использовалось: "Линейное пробирование", а так же
"Пробирование методом двойного хеширования", но первый способ, ни смотря ни на
что, оказался более эффективным в наборе тестовых данных, по этому он был
выбран в качестве итогового, но ниже представлен и другой способ.
Для хранения элементов массива, была создана специальная структура данных,
которая позволяет удобно работать с элементами. А так же в ней есть специальный
атрибут, который позволяет помечать элемент как удалённый, что необходимо для
полной реализации хэш-таблицы.
Размер массива создаваемый при инициализации был увеличен до 20 ** 5,
т.к. сталкивался с проблемой TL с 20 го теста, по результатам исследования
выяснил, что если размер массива равен кол-ву элементов вставляемых в
хэш-таблицу, то результат в 2 раза хуже, чем если при инициализации задаётся
массив большего размера, чем кол-во вставляемых элементов в него.
Причины, почему это так происходит, ясны, для того что бы с этим бороться,
нужно делать рехеширование и перезаписывать массив уже без deleted элементов,
дабы при поиске ключа, не происходило постоянно полного перебирания массива.

# Временная сложность: 0(1). Но при большой заполненности или большом кол-ве
элементов помеченных как deleted может увеличиться до O(n).

# Пространственная сложность: O(k). k - размер массива в хэш-таблице,
размер которого задаётся при инициализации.

# 68656413
import math

def _get_index(self, key: Hashable) -> Iterable[int]:
    key_hash: int = self._get_hash(key)
    h1: int = key_hash % self._m
    f: float = (math.sqrt(5) - 1) / 2
    h2: int = math.floor(
        self._m * (
            f * key_hash - math.floor(f * key_hash)
        )
    )
    i: int = 0
    size: int = 0
    while size < self._m:
        index = (h1 + i * h2) % self._m
        yield index
        i += 1
        size += 1
"""
import sys
from dataclasses import dataclass
from typing import (
    Tuple,
    Any,
    List,
    Iterable,
    Hashable,
    Optional,
    Callable,
    Dict,
)


@dataclass
class _HashItem:
    key: Optional[Hashable] = None
    value: Any = None
    deleted: bool = False


class HashTable:
    def __init__(self, size: int = 20**5) -> None:
        self._m: int = size
        self._data: List[_HashItem] = [_HashItem()] * self._m

    @staticmethod
    def _get_hash(key: Hashable) -> int:
        return hash(key)

    @staticmethod
    def _is_empty_item(item: _HashItem) -> bool:
        return item.key is None

    @staticmethod
    def _is_deleted_item(item: _HashItem) -> bool:
        return item.deleted

    def _get_index(self, key: Hashable) -> Iterable[int]:
        key_hash: int = self._get_hash(key)
        h1: int = key_hash % self._m
        size: int = 0
        while size < self._m:
            if h1 > self._m - 1:
                h1 = 0
            yield h1
            h1 += 1
            size += 1

    def get(self, key: Hashable) -> Optional[Any]:
        index_generator: Iterable[int] = self._get_index(key)
        for idx in index_generator:
            item: _HashItem = self._data[idx]
            if self._is_empty_item(item):
                return None
            if item.key == key and not self._is_deleted_item(item):
                return item.value
        return None

    def _find_index(self, key: Hashable) -> Optional[int]:
        index_generator: Iterable[int] = self._get_index(key)
        item_index: Optional[int] = None
        deleted_item_index: Optional[int] = None
        for idx in index_generator:
            item: _HashItem = self._data[idx]
            if self._is_empty_item(item) or item.key == key:
                item_index = idx
                break
            if self._is_deleted_item(item) and deleted_item_index is None:
                deleted_item_index = idx
        if item_index is not None:
            return item_index
        return deleted_item_index

    def put(self, key: Hashable, value: Any) -> None:
        index: Optional[int] = self._find_index(key=key)
        if index is None:
            raise AssertionError()
        self._data[index] = _HashItem(key=key, value=value)
        return None

    def delete(self, key: Hashable) -> Optional[Any]:
        index: Optional[int] = self._find_index(key=key)
        if (
            index
            and self._data[index].key == key
            and not self._data[index].deleted
        ):
            item: _HashItem = self._data[index]
            item.deleted = True
            return item.value
        return None


class HashTableCommand:
    get: str = "get"
    put: str = "put"
    delete: str = "delete"

    def __init__(
        self,
        hash_table: HashTable,
        func: str,
        key: Hashable,
        value: Optional[int] = None,
    ):
        self.hash_table: HashTable = hash_table
        self.func: str = func
        self.key: Hashable = key
        self.value: Optional[int] = value

    def execute(self) -> Optional[Any]:
        action: Dict[str, Callable] = {
            self.get: self.hash_table.get,
            self.put: self.hash_table.put,
            self.delete: self.hash_table.delete,
        }
        if self.func == self.put:
            action[self.func](self.key, value=self.value)
            return None
        return action[self.func](self.key)


def execute_command(
    hash_table: HashTable, command: Tuple[str, int, Optional[int]]
) -> Optional[Any]:
    func: str = command[0]
    key: Hashable = command[1]
    value: Optional[Any] = command[2]
    return HashTableCommand(
        hash_table=hash_table, func=func, key=key, value=value
    ).execute()


def get_commands(command_length: int) -> List[Tuple[str, int, Optional[int]]]:
    commands: List[Tuple[str, int, Optional[int]]] = []
    for _ in range(command_length):
        data: List[str] = sys.stdin.readline().rstrip().split()
        command: Tuple[str, int, Optional[int]] = (
            data[0],
            int(data[1]),
            int(data[2]) if len(data) > 2 else None,
        )
        commands.append(command)
    return commands


def main() -> None:
    commands_length: int = int(input())
    hash_table: HashTable = HashTable()
    for command in get_commands(commands_length):
        result = execute_command(hash_table, command)
        if command[0] == HashTableCommand.put:
            continue
        print(result)


if __name__ == "__main__":
    main()
