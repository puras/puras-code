第8课 For循环-练习
----

# 知识点

* range的进阶用法

	range(start, stop, step)

说明：

start: 计数从start开始，默认是从0开始  
stop: 计数到stop结束，但不包括stop  
step: 步长，默认为1  

# 示例

* 求1到999的累加和

```
	sum = 0
	for i in range(1000):
		sum += i
	print(sum)
```

* 求1到10的累计乘积

>* 方案一

```
	ret = 1
	for i in range(10):
		ret *= (i + 1)
	print(ret)
```

>* 方案二

```
	ret = 1
	for i in range(11):
		if i > 0:
			ret *= i
	print(ret)
```

>* 方案三

```
	ret = 1
	for i in range(1, 11):
		ret *= i
	print(ret)
```