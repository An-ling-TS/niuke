'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-05 14:34:51
LastEditors: Liang Anqing
LastEditTime: 2020-09-05 14:47:58
'''
'''
题目描述
二货小易有一个W*H的网格盒子，网格的行编号为0~H-1，网格的列编号为0~W-1。每个格子至多可以放一块蛋糕，任意两块蛋糕的欧几里得距离不能等于2。
对于两个格子坐标(x1,y1),(x2,y2)的欧几里得距离为:
( (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) ) 的算术平方根
小易想知道最多可以放多少块蛋糕在网格盒子里。
输入描述:

每组数组包含网格长宽W,H，用空格分割.(1 ≤ W、H ≤ 1000)

输出描述:

输出一个最多可以放的蛋糕数

示例1
输入
复制

3 2

输出
复制

4

'''
def solution(arr):
    w,h=arr
    temp=[[0 for i in range(w)] for j in range(h)]
    rs=0
    for i in range(h):
        for j in range(w):
            if (j-2>=0 and temp[i][j-2]==1) or (i-2>=0 and temp[i-2][j]==1):
                continue
            temp[i][j]=1
            rs+=1
    return rs
if __name__=='__main__':
    arr=list(map(int,input().strip().split()))
    print(solution(arr))