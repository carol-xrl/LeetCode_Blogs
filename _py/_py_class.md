- `__init__(self, para1, para...)` 会被自动调用
- `__method()`或`__variable`形式的为私有变量/方法
- 函数的第一个参数为指向自己的指针`self` (也可以命名为其他)，是定义时必须写的第一个参数
```python
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
s = student('ken',10,60,3)
s.speak()
super(student,c).speak()

# ken 说: 我 10 岁了，我在读 3 年级
```

- 多继承：若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索
```python
class Class_3(Class_1,Class_2):
    a =''
    def __init__(self,n,a,w,g,t):
        Class_1.__init__(self,n,a,w,g)
        Class_2.__init__(self,n,t)
```

- 运算符重载

| 专有方法       | 作用描述                  |
|--------------|-------------------------|
| `__init__`   | 构造函数，在生成对象时调用 |
| `__del__`    | 析构函数，释放对象时使用   |
| `__repr__`   | 打印，转换                |
| `__setitem__`| 按照索引赋值              |
| `__getitem__`| 按照索引获取值            |
| `__len__`    | 获得长度                  |
| `__cmp__`    | 比较运算                  |
| `__call__`   | 函数调用                  |
| `__add__`    | 加运算                    |
| `__sub__`    | 减运算                    |
| `__mul__`    | 乘运算                    |
| `__truediv__`| 除运算                    |
| `__mod__`    | 求余运算                  |
| `__pow__`    | 乘方                      |

```python
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
# 告诉 Python 这个对象该如何在 print() 里展示，让输出更友好
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
# 相当于v1__add__(v2)
```