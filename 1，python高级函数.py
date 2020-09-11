# 1 lambda函数，匿名函数
mypow2 = lambda x: x ** 2

print(mypow2(5))

f1 = lambda x: 'True' if x == 1 else 'False'

print(f1(1), f1(2))
print()

# 2 map函数
"""
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
"""
numlist = [x for x in range(1, 10)]
print(numlist)


def getpow(x):
    return x ** 2


print(list(map(getpow, numlist)))

print(list(map(lambda x: x**2,numlist)))
print()

# 3 reduce函数
"""
reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
"""
from functools import reduce
def add(x,y):
    return x+y

print(numlist)
sum = reduce(add,numlist)
print(sum)

charlist = list("hello world!")
print(charlist)
charsum = reduce(add,charlist)
print(charsum)
print()


#4 filter函
"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
"""
result = filter(lambda x : x%5 == 0,range(100))
print(list(result))
print()


#5 判断数据类型
a = "A"
print(isinstance(a,str))