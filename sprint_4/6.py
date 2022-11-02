def string_compare(first, second):
    if len(first) != len(second):
        return "NO"
    fist_matching = {}
    second_matching = {}
    for idx, symbol in enumerate(first):
        second_symbol = second[idx]
        if (
            fist_matching.get(symbol)
            and fist_matching[symbol] != second_symbol
        ) or (
            second_matching.get(second_symbol)
            and second_matching[second_symbol] != symbol
        ):
            return "NO"
        fist_matching[symbol] = second_symbol
        second_matching[second_symbol] = symbol
    return "YES"


def main():
    first = input()
    second = input()
    print(string_compare(first, second))


main()
