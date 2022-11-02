def get_hash(value: str, a: int, m: int) -> int:
    result: int = 0
    for idx, v in enumerate(value):
        result = (result * a + ord(v)) % m
    return result


def main():
    a: int = int(input())
    m: int = int(input())
    value: str = input()
    result: int = get_hash(value, a, m)
    print(result)


if __name__ == "__main__":
    main()
