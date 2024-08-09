n = int(input())

s = 0
idx = 1
for i in range(1, n + 1, 2):
    if idx % 2 != 0:
        s += 1 / i
    else:
        s -= 1 / i
    idx += 1

print(round(s, 8))