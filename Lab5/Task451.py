s = 0
sum_squares = 0

while True:
    x = int(input())
    s = s + x
    sum_squares = sum_squares + x * x
    if s == 0:
        break
print(sum_squares)