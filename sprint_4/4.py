substring = input()
substring_elements = []
max_size = 0
for i in substring:
    try:
        idx = substring_elements.index(i)
    except ValueError:
        idx = None
    if idx is None:
        substring_elements.append(i)
    else:
        substring_elements = substring_elements[idx + 1 :]
        substring_elements.append(i)
    max_size = max(len(substring_elements), max_size)
print(max_size)
