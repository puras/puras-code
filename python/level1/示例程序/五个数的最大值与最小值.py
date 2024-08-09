x = []
for i in range(5):
    x.append(int(input("请输入第" + str(i + 1) + "个数：")))

max = x[0]
min = x[0]
for i in x:
    if max < i:
        max = i
    if min > i:
        min = i

print("5个数中最大值为: " + str(max) + ", 最小值为：" + str(min))