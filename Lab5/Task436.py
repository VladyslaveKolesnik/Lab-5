line = input()
str_list = line.split()
numbers = []

for s in str_list:
    numbers.append(int(s))
numbers.sort()
print(numbers[1])