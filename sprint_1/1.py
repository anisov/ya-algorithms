input_data = input()
data = list(map(int, input_data.split(" ")))
a = data[0]
x = data[1]
b = data[2]
c = data[3]
result = a * x**2 + b * x + c
print(result)
