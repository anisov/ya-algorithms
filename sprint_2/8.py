from typing import List, Dict, Set

data: List[str] = list(input())


def is_correct_bracket_seq(data: List[str]) -> bool:
    stack: List[str] = []
    seq_equeal: Dict[str, str] = {
        "}": "{",
        "]": "[",
        ")": "(",
    }
    left_seq: Set[str] = set(seq_equeal.values())
    result: bool = True
    for i in data:
        if i in left_seq:
            stack.append(i)
        else:
            if len(stack) == 0:
                result = False
                break
            if seq_equeal[i] != stack.pop():
                result = False
                break
    if len(stack) > 0:
        result = False
    return result


print(is_correct_bracket_seq(data=data))
