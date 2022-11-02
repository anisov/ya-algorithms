# 68671683
# При реализации алгоритма в самом начале необходимо построить индекс,
# затем найти с использованием индекса ответ на запрос. Для построения индекса
# используется специальная структура данных, называемая перевёрнутым индексом,
# которая обеспечивает самый быстрый поиск в поставленной задаче. Его алгоритм
# заключается в том, что бы по ключевому слову вернуть список документов где
# встречается запрашиваемое слово и в каком количестве.

# Временная сложность: 0(n^2) построение индекса. Поиск по запросам. O(n^2)
# Пространственная сложность: O(n).

import heapq
import sys
from collections import (
    Counter,
    defaultdict,
)
from typing import (
    List,
    Tuple,
    Dict,
    Set,
)
from functools import cmp_to_key


class SearchSystem:
    def __init__(self, documents: List[List[str]]):
        self.documents: List[List[str]] = documents

    @staticmethod
    def _relevant_documents_cmp(
        v1: Tuple[int, int], v2: Tuple[int, int]
    ) -> int:
        if v1[1] == v2[1]:
            if v1[0] > v2[0]:
                return -1
            return 1
        if v1[1] > v2[1]:
            return 1
        return -1

    def _create_documents_index(self) -> Dict[str, Dict[int, int]]:
        documents_index: Dict[str, Dict[int, int]] = defaultdict(dict)
        for doc_idx, document in enumerate(self.documents, start=1):
            for world, count in Counter(document).items():
                documents_index[world][doc_idx] = count
        return documents_index

    def _get_sorted_relevant_documents(
        self, relevant_documents: Dict[int, int], relevant_documents_count: int
    ) -> List[int]:
        result: List[int] = []
        for idx, count in heapq.nlargest(
            relevant_documents_count,
            relevant_documents.items(),
            key=cmp_to_key(self._relevant_documents_cmp),  # type: ignore
        ):
            if count > 0:
                result.append(idx)
        return result

    def find_relevant_documents(
        self,
        request_worlds: List[List[str]],
        relevant_documents_count: int,
    ) -> List[List[int]]:
        documents_index: Dict[
            str, Dict[int, int]
        ] = self._create_documents_index()
        result: List[List[int]] = []
        for worlds in request_worlds:
            relevant_documents: Dict[int, int] = defaultdict(int)
            worlds_cache: Set[str] = set()  # Or can use: worlds = set(worlds)
            for world in worlds:
                if world in worlds_cache:
                    continue
                world_documents: Dict[int, int] = documents_index.get(
                    world, {}
                )
                for doc_idx, count in world_documents.items():
                    relevant_documents[doc_idx] += count
                worlds_cache.add(world)
            sorted_docs: List[int] = self._get_sorted_relevant_documents(
                relevant_documents=relevant_documents,
                relevant_documents_count=relevant_documents_count,
            )
            result.append(sorted_docs)
        return result


def get_data() -> Tuple[List[List[str]], List[List[str]]]:
    length: int = int(input())
    documents: List[List[str]] = []
    for _ in range(length):
        documents.append(sys.stdin.readline().rstrip().split())
    length = int(input())
    request_worlds: List[List[str]] = []
    for _ in range(length):
        request_worlds.append(sys.stdin.readline().rstrip().split())
    return documents, request_worlds


def main() -> None:
    documents, request_worlds = get_data()
    result: List[List[int]] = SearchSystem(
        documents=documents
    ).find_relevant_documents(
        request_worlds=request_worlds, relevant_documents_count=5
    )
    for i in result:
        print(*i)


if __name__ == "__main__":
    main()
