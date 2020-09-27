'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-10 17:12:39
LastEditors: Liang Anqing
LastEditTime: 2020-09-10 18:35:29
'''
'''


假设有N个人要玩游戏，每轮游戏必须选出一个人当裁判，剩下的N-1个人作为玩家。现在第i个人要求作为玩家进行至少Ai轮游戏，那么至少需要进行多少轮游戏才能满足所有人的要求？

输入描述:

第一行包含一个整数N，2≤N≤105。

第二行包含N个空格隔开的整数A1到AN，0≤Ai≤109。


输出描述:

输出至少需要进行的游戏轮数。


输入例子1:

3
2 2 3


输出例子1:

4

'''
def solution(n,arr):
    rs=0
    while sum(arr)>0:
        #保存最小值坐标和值
        min_pos=arr.index(min(arr))
        min_val=arr[min_pos]
        if min_val==0:
            rs+=max(arr)
            break
        #获取第二小的值
        if min_pos>0 and min_pos<n-1:
            min_sec=min(arr[0:min_pos]) if min(arr[0:min_pos])<min(arr[min_pos+1:n]) else min(arr[min_pos+1:n])
        elif min_pos==0:
            min_sec=min(arr[1:n])
        elif min_pos==n-1:
            min_sec=min(arr[0:n-1])
        #除最小值外，所有值减(min_sec-min_val+1)
        arr=list(map(lambda x:x-min_sec+min_val-1 if x>0 else x,arr))
        arr[min_pos]=min_val
        #轮数+(min_sec-min_val)
        rs+=(min_sec-min_val+1)
    return rs
if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().strip().split()))
    print(solution(n,arr))