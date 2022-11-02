# 68430845
# Для решения задачи использовался бинарный поиск, так как несмотря на то, что,
# порядок сбит, он всё равно есть, кроме определённых мест, где произошла
# ошибка, и цель алгоритма - это найти ошибку (nums[left] <= nums[middle]), и
# в этот момент изменить поведение, для дальнейшего корректного исполнения
# бинарного поиска. Для решения задачи было решено использовать цикл, а не
# рекурсию, для лучшей производительности.
# Временная сложность: 0(log(n))
# Пространственная сложность: O(1)


def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[left] <= nums[middle]:
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if nums[left] >= target < nums[middle] or target >= nums[left]:
                right = middle - 1
            else:
                left = middle + 1
    return -1
