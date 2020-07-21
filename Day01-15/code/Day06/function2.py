"""
函数的定义和使用 - 求最大公约数和最小公倍数

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""

""" 
def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))
 """
 
def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)      #if-else的简写
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

print(gcd(15,25))
