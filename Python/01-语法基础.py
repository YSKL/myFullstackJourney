# 第一个程序
print('Hello, World!')

print('------------------------------------------------------------')

# 变量：
# 六种基本类型: int（整数）
#             float（浮点数）
#             str（字符串）
#             bool（布尔）：True、False
#             NoneType（None：没有值）
#             bytes（字节）：b"xxx"
a = 33  # int
b = 3.14  # float
c = 'cc'  # str
d = True  # bool
e = None  # NoneType
f = b"fff"  # bytes
print(type(a), type(b), type(c), type(d), type(e), type(f))
# <class 'int'> <class 'float'> <class 'str'> <class 'bool'> <class 'NoneType'> <class 'bytes'>

print('------------------------------------------------------------')

# 运算符：
# 算数运算：+、-、*、/（除）、//（整除）、%（取余数）、**（幂运算）
print(7 + 3)  # 10
print(7 - 3)  # 4
print(7 * 3)  # 21
print(7 / 3)  # 2.333...   /  是普通除法，结果是 float
print(7 // 3)  # 2          // 是整除，丢弃小数
print(7 % 3)  # 1          %  是取余数
print(2 ** 10)  # 1024       ** 是幂运算

# 比较运算：>、==、！=（结果一定是 bool）
print(3 > 2)  # True
print(3 == 3)  # True
print(3 != 4)  # True

# 逻辑运算：and、or、not
print(True and False)  # False  — 都真才真
print(True or False)  # True   — 一真就真
print(not True)  # False  — 取反

# 赋值简写：=、+=、*=
x = 10
x += 5  # 等价 x = x + 5
x *= 2  # 等价 x = x * 2
print(x)  # 30

# 位运算：&（按位与）、｜（按位或）、^（异或）
print(5 & 3)  # 1   按位与
print(5 | 3)  # 7   按位或
print(5 ^ 3)  # 6   异或

print('------------------------------------------------------------')

# 字符串：
# 创建与拼接
str1 = "Hello"
str2 = 'Hello'  # 单双音好好听都行
str3 = """
        床前明月光，
        疑是地上霜.
        举头望明月，
        低头思故乡。
      """  # 三引号，多行字符串
print(str1 + ', ' + str2)  # 拼接
print('ha' * 3)  # haha 重复 3 次 → hahahaha

# 切片
st1 = 'Python'
print(st1[0])  # P 第一个字符（下标从0开始）
print(st1[-1])  # n 最后一个字符
print(st1[0:3])  # Pyt 取0、1、2，不包含3
print(st1[2:])  # thon 从2到结尾
print(st1[::-1])  # nohtyP 反转

# f-string格式化
name = '小刚'
score = 100
print(f"{name} 这次考了{score}分，{'及格' if score >= 60 else '不及格'}")

# 10个常用方法
s = ' Hello Python '
print(s.strip())  # 'Hello Python' 去首尾空格。 str.strip('xxx'):从字符串'两端'开始删除，直到遇到第一个不在指定字符串中的字符就停下。
print(s.lower())  # 全小写
print(s.upper())  # 全大写
print(s.replace("o", "0"))  # 替换
print(s.split())  # ['Hello', 'Python']  按空格分割
print("-".join(["a", "b", "c"]))  # a-b-c  用 - 连接
print("Python".startswith("Py"))  # True
print("Python".endswith("on"))  # True
print("Python".find("th"))  # 2  找不到返回 -1
print(len("Python"))  # 6  长度

print('------------------------------------------------------------')

# input与类型转换
name = input("请输入姓名：")  # 程序停下来等你打字 + 回车
age = input("请输入年龄：")  # 注意：input 拿到的永远是 str ！
print(type(age))  # <class 'str'>
age = int(age)  # 显式转 int
print(f"明年你 {age + 1} 岁")
# 隐式转换：1 + 2.0 Python 自动把 1 升级成 1.0。
# 显式转换：int("3") 你主动告诉 Python 要换。

print('------------------------------------------------------------')

# 分支：if/elif/else
num = int(input('请输入你的成绩：'))
if num >= 90:
    print('A')
elif num >= 80:
    print('B')
elif num >= 60:
    print('C')
else:
    print('不及格')

# 三元表达式
res = '及格' if num >= 60 else '不及格'
print(res)

print('------------------------------------------------------------')

# 循环：while 与 for：知道次数或要遍历元素 → 用 for；不知道次数、按条件循环 → 用 while。
# while
n = 1
while n <= 5:
    print(n)
    n += 1  # 千万别忘！否则死循环

# for + range
# range(起始, 结束, 步长)，左闭右开
for i in range(5):
    print(i)  # 0,1,2,3,4

for i in range(1, 6):
    print(i)  # 1,2,3,4,5

for i in range(0, 10, 2):
    print(i)  # 0,2,4,6,8  步长 2

# break/continue
for i in range(10):
    if i == 3:
        continue  # 跳过本次
    if i == 7:
        break  # 直接退出
    print(i)  # 输出 0 1 2 4 5 6

# 循环 + else
# 循环正常结束（没被 break 打断）才执行 else
for i in range(3):
    print(i)
else:
    print("循环正常执行完毕")

# 嵌套循环（九九乘法表）
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}", end=" ")
    print()

print('------------------------------------------------------------')

# BMI计算器
height = float(input('请输入身高（米）：'))
weight = float(input('请输入体重（千克）：'))
bmi = weight / (height ** 2)

if bmi < 18.5:
    level = '偏瘦'
elif bmi < 24:
    level = '正常'
elif bmi < 28:
    level = '超重'
else:
    level = '肥胖'
print(f"你的BMI是{bmi:.2f}，属于{level}")

print('------------------------------------------------------------')

# 猜数字游戏
import random

num = random.randint(1, 100)
count = 0
while True:
    guess = int(input('猜 1-100：'))
    count += 1
    if guess < num:
        print('猜小了')
    elif guess > num:
        print('猜大了')
    else:
        print(f"恭喜猜对，一共猜了{count}次")
        break
