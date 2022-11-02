data: str = input()
result = True
last_index = len(data) - 1
for i, v in enumerate(data):
    if not v.isdigit() and not v.isalpha():
        continue
    while not (data[last_index].isdigit() or data[last_index].isalpha()):
        last_index -= 1
    if data[last_index].lower() != v.lower():
        result = False
        break
    last_index -= 1
print(result)
