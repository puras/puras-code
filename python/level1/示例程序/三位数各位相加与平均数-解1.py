x = int(input("请输入一个三位数："))

a = x % 10
b = x // 10 % 10
c = x // 100

s = a + b + c
print("三个数的和是：" + str(s) + ", 三个数的平均数是：" + str(s // 3))