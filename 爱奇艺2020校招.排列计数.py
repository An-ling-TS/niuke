'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-10 17:54:50
LastEditors: Liang Anqing
LastEditTime: 2020-09-10 18:36:54
'''
'''


给定一个大小为N-1且只包含0和1的序列A1到AN-1，如果一个1到N的排列P1到PN满足对于1≤i<N，当Ai=0时Pi<Pi+1，当Ai=1时Pi>Pi+1，则称该排列符合要求，那么有多少个符合要求的排列？

输入描述:

第一行包含一个整数N，1<N≤1000。

第二行包含N-1个空格隔开的整数A1到AN-1，0≤Ai≤1。


输出描述:

输出符合要求的排列个数对109+7取模后的结果。


输入例子1:

4
1 1 0


输出例子1:

3


例子说明1:

符合要求的排列为{3 2 1 4}、{4 2 1 3}和{4 3 1 2}。

'''
def solution(n,arr):
    pass
if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().strip().split()))
    print(solution(n,arr))