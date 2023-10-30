第8课 For循环
----

# 知识点

* range方法

range(n)返回n-1的整数序列，如range(5)生成的序列是从0开始小于5的整数，即0，1，2，3，4。

* for循环写法

```
    for i in range(3):
        print(i)
```

其中：  
    `for`为关键字；    
    i是变量，习惯使用i，可以命名为其他，如j，k等；   
    in是关键字；   
    range()生成循环序列；   
    :为循环开始；     
    下面的print(i)为for循环的语句块，可多行； 注意语句块需要有缩进    
    for循环可以多层嵌套使用。

# 示例

* 三角形 

```
    import turtle as t
    t.shape('turtle')

    for i in range(3):
        t.fd(100)
        t.lt(120)
```

* 五角星

```
    import turtle as t
    t.shape('turtle')

    for i in range(5):
        t.fd(100)
        t.rt(144)
```

* 六边形

```
    import turtle as t
    t.shape('turtle')

    for i in range(6):
        t.fd(100)
        t.rt(60)
```

* 方形螺旋体

```
    import turtle as t
    t.shape('turtle')
    t.speed(10)

    len = 1
    for i in range(200):
        t.fd(len)
        t.lt(90)

        len += 2
```