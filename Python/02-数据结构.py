# 列表list：会变长的购物车
# 创建与索引
fruits = ['苹果', '香蕉']
print(fruits[0])  # 苹果
print(fruits[-1])  # 香蕉
print(len(fruits))  # 2

# 切片（同字符串）
nums = [10, 20, 30, 40, 50]
print(nums[1:4])  # [20, 30, 40]
print(nums[::-1])  # [50, 40, 30, 20, 10] 反转

# 增删改查
# 增
fruits.append('橘子')  # 末尾追加 → ['苹果','香蕉','橘子']
fruits.insert(1, '葡萄')  # 在下标 1 插入 → ['苹果','葡萄','香蕉','橘子']
fruits.extend(['梨', '桃'])  # 追加多个
print(fruits)

# 删
fruits.remove('香蕉')  # 按值删除（删第一个匹配的）
last = fruits.pop()  # 弹出最后一个并返回
del fruits[0]  # 按下标删

# 改
fruits[0] = '西瓜'

# 查
print('西瓜' in fruits)  # True / False
print(fruits.index('梨'))  # 返回下标
print(fruits.count('梨'))  # 出现次数

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
point = (3, 4)
print(point[0], point[1])  # 3 4

# point[0] = 10   # 报错 TypeError

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
person = {'name': '李雷', 'age': 18, 'city': '北京'}
print(person['name'])  # 李雷
person['age'] = 19  # 修改
person['job'] = '学生'  # 新增
del person['city']  # 删除
print(person)  # {'name': '李雷', 'age': 19, 'job': '学生'}
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

# 练习：词频统计
# 统计句子 "the quick brown fox jumps over the lazy dog the end" 里每个单词出现的次数。
sentence = 'the quick brown fox jumps over the lazy dog the end'
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'end': 1}

print('------------------------------------------------------------')

# 集合set：天生去重
nums = [1, 1, 2, 3, 3, 4]
unique = set(nums)
print(unique)  # {1, 2, 3, 4}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # 并集 {1, 2, 3, 4, 5, 6}
print(a & b)  # 交集 {3, 4}
print(a - b)  # 差集 {1, 2}
print(a ^ b)  # 对称差 {1, 2, 5, 6}

# 增
a.add(10)
# 删
a.discard(1)  # 不存在不报错
a.remove(2)  # 不存在会报错
print(a)

# frozenset：不可变集合
fs = frozenset([1, 2, 3, 3, 5])
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
