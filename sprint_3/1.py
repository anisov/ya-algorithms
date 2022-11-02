def bracket(count: int, s: str = "", left: int = 0, right: int = 0):
    if left == count and right == count:
        print(s)
        return
    if left != count:
        bracket(count, s + "(", left + 1, right)
    if right < left:
        bracket(count, s + ")", left, right + 1)


n: int = int(input())
bracket(n)
