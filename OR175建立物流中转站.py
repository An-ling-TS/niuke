'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-22 13:44:03
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-22 14:37:31
'''
'''
题目描述

Shopee物流会有很多个中转站。在选址的过程中，会选择离用户最近的地方建一个物流中转站。

假设给你一个二维平面网格，每个格子是房子则为1，或者是空地则为0。找到一个空地修建一个物流中转站，使得这个物流中转站到所有的房子的距离之和最小。 能修建，则返回最小的距离和。如果无法修建，则返回 -1。

若范围限制在100*100以内的网格，如何计算出最小的距离和？

当平面网格非常大的情况下，如何避免不必要的计算？
输入描述:

4
0 1 1 0
1 1 0 1
0 0 1 0
0 0 0 0

先输入方阵阶数，然后逐行输入房子和空地的数据，以空格分隔。

输出描述:

8

能修建，则返回最小的距离和。如果无法修建，则返回 -1。

示例1
输入
复制

4
0 1 1 0
1 1 0 1
0 0 1 0
0 0 0 0

输出
复制

8

示例2
输入
复制

4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1

输出
复制

-1


'''
'''
思路：
提前求出每行每列房子数量及个房子到0,0的距离和
遍历数组，如果为一则跳过，
否则-》
    将中转站从0,0移动至i，j并计算移动后的新距离，结果取移动前和移动后的较小值
'''
def solution(n,arr):
    row=[0 for i in range(n)]#每行房子数
    col=[0 for i in range(n)]#每列房子数
    res=-1
    S=0#距离
    #到0,0距离
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                S+=i+j
                row[i]+=1
                col[j]+=1
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                continue
            s=S
            for r in range(n):
                if r<j:
                    s=s+(j-2*r)*col[r]
                elif r>=j:
                    s=s-j*col[r]
                if r<i:
                    s=s+(i-2*r)*row[r]
                elif r>=i:
                    s=s-i*row[r]
            if res==-1:
                res=s
            else:
                res=min(res,s)
    return res

if __name__=='__main__':
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().strip().split())))
    print(solution(n,arr))