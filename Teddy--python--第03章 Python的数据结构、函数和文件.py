import pandas as pd
#元组
#元组是一个固定长度，不可改变的Python序列对象。创建元组的最简单方式，是用逗号分隔一列值：
tup = 4,5,6
print(tup)

#当用复杂的表达式定义元组，最好将值放到圆括号内，如下所示：
nested_tup = (4,5,6),(7,8)
print(nested_tup)

#用tuple可以将任意序列或迭代器转换成元组：
tup = tuple([4,0,2])
print(tup)
print(tup[0])
tup = tuple('string')
print(tup)
#可以用方括号访问元组中的元素。和C、C++、JAVA等语言一样，序列是从0开始的：
print(tup[0])

#元组中存储的对象可能是可变对象。一旦创建了元组，元组中的对象就不能修改了：
tup = tuple(['foo',[1,2],True])
#tup[2] = False

#如果元组中的某个对象是可变的，比如列表，可以在原位进行修改
tup[1].append(3)
print(tup)

#可以用加号运算符将元组串联起来：
_t1=(4,None,'foo')+(6,0)+('bar',)
print(_t1)

#元组乘以一个整数，像列表一样，会将几个元组的复制串联起来：
_t2 = ('foo','bar') * 4
print(_t2)

_t3 = pd.read_sas('C:\Program Files\SASHome\SASFoundation\9.4\hps\sample\hmeq.sas7bdat')
print(_t3)