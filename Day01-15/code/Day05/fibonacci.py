"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')


# 递归求fibonacci数列

def fibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fibonacci(N-1)+fibonacci(N-2)

print(fibonacci(20))