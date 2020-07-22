""" 
这个题是来自廖雪峰python教程中的生成器一节的练习题：
关于关键字yield生成生成器的练习
"""

def triangles():
    current = [1]
    yield current
    current = [1,1]
    yield current
    current_left = 0
    current_right = 0
    while True:
        next = []
        for index in range(len(current)):
            if index == 0:
                next.append(current[index]+current_left)
                next.append(current[index]+current[index+1])
            elif index == len(current)-1:
                next.append(current[index]+current_right)
            else:
                next.append(current[index]+current[index+1])
        yield next
        current = next[:]

def main():
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n += 1
        if n == 10:
            break
    
    for t in results:
        print(t)

if __name__ == '__main__':
    main()