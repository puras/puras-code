x = input("请输入一个三位数：")

s = 0

for i in x:
    s += int(i)

print("三个数的和是：" + str(s) + ", 三个数的平均数是：" + str(s // 3))