# 69491376
# Сначала необходимо построить префиксное дерево по набору шаблонов, это
# позволит нам максимально эффективно понять, состоит ли данный текст из этих
# шаблонов. Префиксное дерево будет иметь два необходимых атрибута, является ли
# нода терминальным узлом и список рёбер куда можно совершить переход.
# Далее мы будем по одной перебирать стартовые позиции, к которым можно
# «приложить» шаблон(данное префиксное дерево), проверять на каждом шаге мы
# весь шаблон в целом. Символы строки будут задавать путь по префиксному
# дереву. Если путь по существующим рёбрам дерева проложить не удаётся, шаблон
# в текущей стартовой позиции не подходит. Для хранения промежуточных
# результатов будем использовать массив dp, в котором будут помечаться
# последние символы слов найденные в боре.
# Также если последнее слово было найдено, т.е последний символ был помечен
# как True, то поиск можно прекратить и не проводить дальнейший
# перебор(if dp[-1]: return True).
# Временная сложность: O(L) построение префиксного дерева, где L - сумма длин
# всех шаблонов. O(n*M) где n — длина текста, а M длина самого длинного из
# искомых шаблонов
# Пространственная сложность: O(L), где L - сумма длин всех шаблонов. + O(n),
# где n количество символов в тексте(массив dp)
import sys
from typing import (
    Dict,
    List,
)


class Node:
    def __init__(self) -> None:
        self.edges: Dict[str, Node] = {}
        self.is_terminal: bool = False


class FindAllTextPatterns:
    def __init__(self, text: str, patterns: List[str]) -> None:
        self.text: str = text
        self.patterns: List[str] = patterns

    def _create_tree(self) -> Node:
        """Строим префиксное дерево по набору шаблонов patterns
        :return:
        """
        root: Node = Node()
        for pattern in self.patterns:
            node: Node = root
            for _, v in enumerate(pattern):
                next_node: Node = node.edges.get(v, Node())
                node.edges[v] = next_node
                node = next_node
            node.is_terminal = True
        return root

    def process(self) -> bool:
        root: Node = self._create_tree()
        text_length: int = len(self.text)
        dp: List[bool] = [False] * (text_length + 1)
        dp[0] = True
        for i in range(text_length):
            node: Node = root
            if dp[-1]:
                return True
            if dp[i]:
                for j in range(i, text_length + 1):
                    if node.is_terminal:
                        dp[j] = True
                    if j == text_length or self.text[j] not in node.edges:
                        break
                    node = node.edges[self.text[j]]
        return dp[-1]


def main() -> None:
    text: str = input()
    pattern_count: int = int(input())
    patterns: List[str] = []
    for i in range(pattern_count):
        patterns.append(sys.stdin.readline().rstrip())
    result: bool = FindAllTextPatterns(text=text, patterns=patterns).process()
    print("YES" if result else "NO")


if __name__ == "__main__":
    main()
