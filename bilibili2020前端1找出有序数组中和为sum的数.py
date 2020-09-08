'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-17 16:04:58
LastEditors: Liang Anqing
LastEditTime: 2020-08-17 16:17:09
'''
'''


时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M
找出有序数组（从小到大排列）中和为sum的两个数，要求复杂度为O(n)，找到一组即可

输入描述:

第一行：数组长度
第二行：数组各项的值
第三行：sum


输出描述:

若存在，输出和为sum的两个数，以空格分隔；若不存在，输出notfound


输入例子1:

5
1 3 4 6 8
10


输出例子1:

4 6


输入例子2:

5
1 3 4 6 8
13


输出例子2:

notfound

'''

def solution(n,arr,target):
    if  target<arr[0]:
        print('notfound')
        return 
    for i in range(n):
        if i>0 and arr[i-1]==arr[i]:
            continue
        if target-arr[i] in arr:
            print(arr[i],end=" ")
            print(target-arr[i],end="")
            return
    print('notfound')
if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().strip().split()))
    target=int(input())
    solution(n,arr,target)
                