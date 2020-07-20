"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
import math

for num in range(1, 1000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):    # factor 从 1 遍历到根号 num 
        if num % factor == 0:                           # 能被 num整除的 factor
            result += factor                            
            if factor > 1 and num // factor != factor:  # 找出大于根号 num 的真因子，
                result += num // factor                 # 那么就派出了num和根号num本身
    if result == num:
        print(num)
