import collections


def effective_solution(target, nums):
    nums.sort()
    result = []
    lookup = collections.defaultdict(list)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            is_duplicated = False
            for x, _ in lookup[nums[i] + nums[j]]:
                if nums[i] == nums[x]:
                    is_duplicated = True
                    break
            if not is_duplicated:
                lookup[nums[i] + nums[j]].append([i, j])
    fourth = set()
    for c in range(2, len(nums)):
        for d in range(c + 1, len(nums)):
            value = target - nums[c] - nums[d]
            if value in lookup:
                for a, b in lookup[target - nums[c] - nums[d]]:
                    if b < c:
                        data = (nums[a], nums[b], nums[c], nums[d])
                        if data not in fourth:
                            fourth.add(data)
                            result.append(data)
    return sorted(result)


def main():
    _ = input()
    target = int(input())
    data = list(map(int, input().split()))
    result = effective_solution(target, data)
    print(len(result))
    for i in result:
        print(*i, sep=" ")


if __name__ == "__main__":
    main()
