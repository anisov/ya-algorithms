def is_sub_seq(s1: str, s2: str):
    idx: int = -1
    for i in s1:
        while idx < len(s2) - 1:
            idx += 1
            if i == s2[idx]:
                break
        else:
            return False
    return True


print(is_sub_seq(input(), input()))
