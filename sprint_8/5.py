even = {"b", "d", "f", "h", "j", "l", "n", "p", "r", "t", "v", "x", "z"}


def compare_strings(s1: str, s2) -> int:
    s1_normalization: str = ""
    s2_normalization: str = ""
    for i in s1:
        if i in even:
            s1_normalization += i
    for i in s2:
        if i in even:
            s2_normalization += i
    if s1_normalization > s2_normalization:
        return 1
    elif s1_normalization < s2_normalization:
        return -1
    return 0


def main() -> None:
    s1: str = input()
    s2: str = input()
    print(compare_strings(s1, s2))


if __name__ == "__main__":
    main()
