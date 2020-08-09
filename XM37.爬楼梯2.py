'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-09 16:42:38
LastEditors: Liang Anqing
LastEditTime: 2020-08-09 17:01:22
'''
'''
题目描述
在你面前有一个n阶的楼梯(n>=100且n<500)，你一步只能上1阶或3阶。
请问计算出你可以采用多少种不同的方式爬完这个楼梯（到最后一层为爬完）。
(注意超大数据)
输入描述:

一个正整数，表示这个楼梯一共有多少阶

输出描述:

一个正整数，表示有多少种不同的方式爬完这个楼梯

示例1
输入
复制

100

输出
复制

24382819596721629

'''
def solution(n):
    dp=[0 for i in range(n+1)]
    if n<=3:
        return 1 if b<=2 else 2
    dp[1]=1
    dp[2]=1
    dp[3]=2
    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-3]
    return dp[n]
if __name__=='__main__':
    n=int(input())
    print(solution(n))