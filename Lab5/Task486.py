a, b, c = map(int, input().split())
array_3d = []

for i in range(a):
    layer = []
    for j in range(b):
        row = []
        for k in range(c):
            row.append(0)
        layer.append(row)
    array_3d.append(layer)
print(array_3d)