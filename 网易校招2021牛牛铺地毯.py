'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-08 15:52:15
LastEditors: Liang Anqing
LastEditTime: 2020-08-08 16:34:00
'''
'''
思路：
1.将瓷砖组合或者旋转，定义出新瓷砖2*1,并放弃使用瓷砖1*2
2.问题转化为：获取一个序列,序列中的每一项为3，且序列和为n-k,k=n%3，每个2*3砖块（加上本身）
有4种替换方式，则结果为k*((n-k)/3)*4^((n-k)/3)
'''
def getRes(n):
    k=n%3
    if k>0:
        res=k*((n-k)/3)*pow(4,((n-k)/3))
    else:
        res=pow(4,((n-k)/3))
    return res%10007
def solution(arr):
    res=[]
    for i in arr:
        res.append(getRes(i))
    for i in res:
        print(i)
if __name__=='__main__':
    t=int(input())
    arr=[]
    for i in range(t):
        arr.append(int(input()))
    solution(arr)