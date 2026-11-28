# 列表list：会变长的购物车
# 创建与索引
l1 = []
l2 = list()
print(l1, l2)

fruits = ['苹果', '香蕉']
print(fruits[0])  # 苹果
print(fruits[-1])  # 香蕉
print(len(fruits))  # 2

# 切片（同字符串）
# 语法：序列[起始索引:结束索引:步长] 不改变原数据，返回新数据。返回的数据中不包括结束索引位置的值。
# 起始索引：默认从头开始（下标0）
# 结束索引：默认截取到末尾（容器中元素总个数）
# 步长：默认为1
# 序列包括：列表、元组、字符串
# 当起始索引大于结束索引时，步长必须为负数，否则结果是空列表。
nums = [10, 20, 30, 40, 50]
print(nums[1:4])  # [20, 30, 40]
print(nums[::-1])  # [50, 40, 30, 20, 10] 反转

# 增删改查
# 增
fruits.append('橘子')  # 末尾追加 → ['苹果','香蕉','橘子']
fruits.insert(1, '葡萄')  # 在下标 1 插入 → ['苹果','葡萄','香蕉','橘子']
fruits.extend(['梨', '桃'])  # 追加多个，extend中传入的是可迭代对象
print(fruits)

# 删
fruits.remove('香蕉')  # 按值删除（删第一个匹配的）
last = fruits.pop()  # 弹出最后一个并返回。fruits.pop(下标) 删除指定位置的元素，并将删除的元素返回
# fruits.clear() 删除列表中的所有元素（变成一个空列表）
del fruits[0]  # 按下标删

# 改
fruits[0] = '西瓜'

# 查
# 列表[下标]

# 常用方法
print('西瓜' in fruits)  # True / False
print(fruits.index('梨'))  # 返回元素的下标
print(fruits.count('梨'))  # 返回元素出现的次数
fruits.reverse() # 反转列表（会改变原列表）
print(fruits)
nums = [20, 32, 10, 30, 18, 22, 11]
# nums.sort(reverse=布尔值) # 对列表排序（会改变原列表。默认从小到大，若想从大到小，需将reverse参数设置为True）
nums.sort()
print(nums)

# 常用内置函数
# sorted(数据容器, reverse=布尔值) # 对容器排序（不会改变原数据，返回排序后的新数据。默认从小到大，若想从大到小，需将reverse参数设置为True）
# len(数据容器) # 返回容器中元素的个数
# max(数据容器) # 返回容器中或多个值中的最大值
# min(数据容器) # 返回容器中或多个值中的最小值
# sum(数据容器) # 对容器中所有元素求和（字符串不能使用sum）

# 序列的其他操作
# 相加：新序列 = 序列1 + 序列2 （两个同类型的序列才能相加：字符串+字符串、列表+列表、元组+元组）
# 相乘：新序列 = 序列 * n (n必须是整数，不能是浮点数。序列中的内容重复n次)

# 列表推导式
# 普通写法
squares = []
for i in range(1, 6):
    squares.append(i * i)

# 推导式写法（一行搞定）
# 列表推导式 = [表达式 for 元素 in 可迭代对象 if 条件]，比 for 循环更短更快。
squares = [i * i for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# 带筛选
evens = [i for i in range(20) if i % 2 == 0]
print(evens)  # [0, 2, 4, ..., 18]

# 双层循环
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)  # [(1,3),(1,4),(2,3),(2,4)]

# 练习：
# 给定 lists = [3, 1, 4, 1, 5, 9, 2, 6]，用一行代码：
lists = [3, 1, 4, 1, 5, 9, 2, 6]
# 1. 取出所有偶数
res1 = [i for i in lists if i % 2 == 0]
print(res1)
# 2. 把每个数字平方
res2 = [i ** 2 for i in lists]
print(res2)

print('------------------------------------------------------------')

# 元组tuple：一旦决定就不能改的清单
# 定义
t1 = ()
t2 = tuple()
print(t1, t2)

# 定义一个元素的元组
t3 = (1,)
t4 = (2,)

point = (3, 4)
print(point[0], point[1])  # 3 4

# point[0] = 10   # 报错 TypeError

# 元组中的元素，不可修改，但是元组中如果存放了可变类型（列表），那可变类型中的内容仍可修改。
t = (1, 3, [3, 5])
t[2][1] = 4
print(t)

# 常用方法
# 元组.index(元素)
# 元组.count(元素)

# 常用内置函数
# max(元组)
# min(元组)
# len(元组)
# sorted(元组) 返回值是列表
# sum(元组) 元组中的元素必须是数字

# 解包
x, y = point
print(x, y)  # 3 4

# 一行交换两个变量
a, b = 1, 2
a, b = b, a
print(a, b)  # 2 1

# namedtuple：给位置起名字
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # 1 2

# 何时用 tuple？
# 数据不变且位置有意义（比如坐标、日期）的时候。

print('------------------------------------------------------------')

# 字典 dict：键值对档案柜
# 基本用法
person = {}
person = dict()
person = {'name': '李雷', 'age': 18, 'city': '北京'}
print(person['name'])  # 李雷
person['age'] = 19  # 修改
person.update({'name': '李李', 'age': 20}) # 批量修改
person['job'] = '学生'  # 新增
del person['city']  # 删除
print(person)  # {'name': '李李', 'age': 20, 'job': '学生'}
print('name' in person)  # True

# 安全的查找：get/setdefault
score = {'小明': 90}

# print(score['小黑'])      # KeyError
print(score.get('小黑'))  # None  键不存在时返回 None
print(score.get('小黑', 0))  # 0 给个默认值

# setdefault: 没有就新增，有就返回
score.setdefault('小黑', 80)
print(score)  # {'小明': 90, '小黑': 80}

# 遍历
for key in person:  # 默认遍历键
    print(key)

for key, value in person.items():  # 同时拿键和值
    print(key, value)

print(list(person.keys()))  # ['name', 'age', 'job']
print(list(person.values()))  # ['李雷', 19, '学生']

# 字典推导式
nums = [1, 2, 3, 4]
square_map = {num: num * num for num in nums}
print(square_map)  # {1: 1, 2: 4, 3: 9, 4: 16}

# 找到最贵的水果
fruits1 = {
    '苹果': 4.5,
    '香蕉': 3.2,
    '橙子': 5.8,
    '草莓': 12.0,
    '哈密瓜': 8.8
}
key = max(fruits1, key=fruits1.get)
print(f'最贵的水果是{key}，价格是{fruits1[key]}')

# 练习：词频统计
# 统计句子 "the quick brown fox jumps over the lazy dog the end" 里每个单词出现的次数。
sentence = 'the quick brown fox jumps over the lazy dog the end'
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'end': 1}

print('------------------------------------------------------------')

# 集合set：天生去重，可变集合
s1 = set()
# 集合中【不能】嵌套【可变集合】，但【可以】嵌套【不可变集合】。
# 只有【不可变】的东西，才能放进集合。

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 数学运算
print(a | b)  # 并集 {1, 2, 3, 4, 5, 6}
print(a & b)  # 交集 {3, 4}
print(a - b)  # 差集 {1, 2}
print(a ^ b)  # 对称差 {1, 2, 5, 6}

# 增
a.add(10) # 向集合中添加元素
a.update(b) # 向集合中批量添加元素（接收可迭代对象，例如：列表、元素、集合）

# 删
a.discard(1)  # 从集合中移除制定元素，元素不存在不会报错，无返回
a.remove(2)  # 从集合中移除制定元素，元素不存在会报错，无返回
a.pop() # 从集合中移除一个任意元素，返回移除的元素
# a.clear() # 清空集合，无返回
print(a)

# 改
# 通过 remove + add 的组合，来实现修改的效果

# 查
# 通过成员运算符（in/not in），判断某个元素是否在集合中

# 常用方法
# 集合A.difference(集合B) # 找出集合A中，不同于集合B的元素（集合A与集合B都不变），返回一个新的集合
# 集合A.difference_update(集合B) # 从集合A中，删除集合B中存在的元素（集合A会被修改，而集合B不会），无返回值
# 集合A.union(集合B) # 合并两个集合，集合A和B都不变，返回一个新集合
# 集合A.issubset(集合B) # 判断集合A是否是集合B的子集，如果集合A中的所有元素都在集合B中，就返回True，否则返回False
# 集合A.issuperset(集合B) # 判断集合A是否是集合B的超集，如果集合A中包含了集合B中的所有元素，就返回True，否则返回False
# 集合A.isdisjiont(集合B) # 判断集合A和集合B是否没有交集，如果没有交集就返回True，但凡有一个公共元素，就返回False

# 集合的循环遍历：使用for循环。集合中的元素没有固定顺序，无法通过下标访问。

# frozenset：不可变集合。接收的参数可以是任意可迭代对象，但最终的返回一定是【不可变集合】
fs = frozenset([1, 2, 3, 3, 5])
fs = frozenset((1, 2, 3, 3, 5))
fs = frozenset({1, 2, 3, 3, 5})
# fs.add(4)   # 不能改
# 可以作为 dict 的键、放进 set 里

print('------------------------------------------------------------')

# 字符串高级：正则re入门
import re

text = '我的电话是 13800138000,他的电话是 13912345678'
phones = re.findall(r'1[3-9]\d{9}', text)
print(phones)  # ['13800138000', '13912345678']

# 常用元字符
# \d  数字  
# \w 字母数字下划线  
# \s 空白
# .   任意字符
# +   1 个或多个   
# *  0 个或多个   
# ? 0 或 1
# {n} 恰好 n 个    
# {n,m} n 到 m 个

# 替换
print(re.sub(r'\d', '*', 'abc123'))  # abc***

print('------------------------------------------------------------')

# 容器对比表
# 容器        有序        可变      可重复     索引方式        典型用途
# list        ✅         ✅        ✅        下标          顺序集合
# tuple       ✅         ❌        ✅        下标          不变的记录
# dict        ✅(3.7+)   ✅        键唯一      键           映射查找
# set         ❌         ✅        ❌         无           去重/集合运算
# frozenset   ❌         ❌        ❌         无           作为dict键

print('------------------------------------------------------------')

# 内存视角：可变 VS 不可变
# 不可变：改了 = 创建新对象
a = "hello"
print(id(a))     # 比如 4400000000
a = a + " world"
print(id(a))     # id 变了！其实是新对象

# 可变：原地修改，id 不变
lst = [1, 2, 3]
print(id(lst))   # 比如 4500000000
lst.append(4)
print(id(lst))   # 还是 4500000000

# 坑！默认参数是可变对象
def add(item, target=[]):     # ❌ 危险
    target.append(item)
    return target

print(add(1))   # [1]
print(add(2))   # [1, 2]  — 共享了同一个列表！
# 函数默认参数永远不要写可变对象，用 `target=None` 然后在函数里判断。

print('------------------------------------------------------------')

# 词频统计：升级版
import re
from collections import Counter

text = """
Python is great Python is easy Python is fun
We love Python because Python makes life easy
"""

words = re.findall(r"\w+", text.lower())   # 全部小写并提取单词
counter = Counter(words)
print(counter.most_common(3))   # [('python', 5), ('is', 3), ('easy', 2)]

print('------------------------------------------------------------')

# 学生成绩管理
students = []  # 每个元素是 dict

def add_student(name, math, en):
    students.append({"name": name, "math": math, "en": en})

add_student("小明", 90, 85)
add_student("小红", 78, 92)
add_student("小刚", 65, 70)

# 平均分
for s in students:
    s["avg"] = (s["math"] + s["en"]) / 2

# 按平均分排序
students.sort(key=lambda s: s["avg"], reverse=True)

for s in students:
    print(f"{s['name']:>4}  数学{s['math']}  英语{s['en']}  平均{s['avg']:.1f}")

print('------------------------------------------------------------')

# ASCII 词云
from collections import Counter

text = "apple banana apple orange banana apple apple orange grape"
counter = Counter(text.split())

for word, n in counter.most_common():
    print(f"{word:<8} {'#' * n}  ({n})")

# 运行结果
# apple    ####  (4)
# banana   ##  (2)
# orange   ##  (2)
# grape    #  (1)
