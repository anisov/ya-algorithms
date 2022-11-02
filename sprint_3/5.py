_ = input()
input_data = input().split()


def things_sort(data, k):
    things = [0] * k
    for i in data:
        things[int(i)] += 1
    result = []
    for i, v in enumerate(things):
        result.extend([i] * v)
    return result


print(*things_sort(data=input_data, k=3), sep=" ")
