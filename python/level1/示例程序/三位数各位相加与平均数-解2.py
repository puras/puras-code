x = input("请输入一个三位数：")

a = int(x[0:1])
b = int(x[1:2])
c = int(x[2:3])

s = a + b + c
print("三个数的和是：" + str(s) + ", 三个数的平均数是：" + str(s // 3))