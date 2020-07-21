'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-21 15:52:42
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-21 15:56:32
'''
'''
题目描述

输入一个整形数组（可能有正数和负数），求数组中连续子数组（最少有一个元素）的最大和。要求时间复杂度为O(n)。
输入描述:

【重要】第一行为数组的长度N（N>=1）

接下来N行，每行一个数，代表数组的N个元素

输出描述:

最大和的结果

示例1
输入
复制

8
1
-2
3
10
-4
7
2
-5

输出
复制

18

说明

最大子数组为 3, 10, -4, 7, 2


'''
def solution(n,arr):
    dp=[i for i in arr]
    for i in range(n):
        for j in range(i,n):
            dp[i]=max(dp[i],sum(arr[i:j+1]))
            print(dp[i])
        
    return max(dp)
if __name__=='__main__':
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(solution(n,arr))