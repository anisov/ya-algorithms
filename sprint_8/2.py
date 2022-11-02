def border_control(s1: str, s2: str, mistakes_count: int) -> str:
    if abs(len(s1) - len(s2)) > mistakes_count:
        return "FAIL"
    id1: int = 0
    id2: int = 0
    mistakes: int = 0
    while id1 < len(s1) and id2 < len(s2):
        if s1[id1] == s2[id2]:
            id1, id2 = id1 + 1, id2 + 1
            continue
        mistakes += 1
        if mistakes > mistakes_count:
            return "FAIL"
        if len(s1[id1:]) == len(s2[id2:]):
            id1, id2 = id1 + 1, id2 + 1
        elif len(s1[id1:]) < len(s2[id2:]):
            id2 += 1
        else:
            id1 += 1
    return "OK"


def main() -> None:
    print(border_control(input(), input(), 1))


if __name__ == "__main__":
    main()
