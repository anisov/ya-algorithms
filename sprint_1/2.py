def get_is_event_number(number: int):
    return number % 2 == 0


input_data: str = input()
data: list = input_data.split(" ")
even_state: bool = get_is_event_number(int(data[0]))

result: str = ""

for i in data:
    is_even: bool = get_is_event_number(int(i))
    if even_state != is_even:
        result = "FAIL"
        break
    result = "WIN"

print(result)
