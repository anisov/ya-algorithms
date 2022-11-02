_ = input()
children = list(reversed(sorted(map(int, input().split()))))
_ = input()
cookies = list(reversed(sorted(map(int, input().split()))))

result = 0
cookie_idx = 0
for i, v in enumerate(children):
    if len(cookies) - 1 >= cookie_idx and v <= cookies[cookie_idx]:
        cookie_idx += 1
        result += 1

print(result)
