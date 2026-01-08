line = input()
str_list = line.split()
numbers = []

for x in str_list:
    numbers.append(int(x))

for i in range(1, len(numbers)):
    if numbers[i] * numbers[i-1] > 0:
        print(numbers[i-1], numbers[i])
        