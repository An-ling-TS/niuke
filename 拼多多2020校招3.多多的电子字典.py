'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-07 16:43:23
LastEditors: Liang Anqing
LastEditTime: 2020-09-07 16:44:45
'''
'''
[编程题]多多的电子字典

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M
多多鸡打算造一本自己的电子字典，里面的所有单词都只由a和b组成。
每个单词的组成里a的数量不能超过N个且b的数量不能超过M个。
多多鸡的幸运数字是K，它打算把所有满足条件的单词里的字典序第K小的单词找出来，作为字典的封面。

输入描述:

共一行，三个整数N, M, K。(0 < N, M < 50, 0 < K < 1,000,000,000,000,000)


输出描述:

共一行，为字典序第K小的单词。


输入例子1:

2 1 4


输出例子1:

ab


例子说明1:

满足条件的单词里，按照字典序从小到大排列的结果是
a
aa
aab
ab
aba
b
ba
baa

'''
def solution(arr):
    n,m,k=arr
    
if __name__=='__main__':
    arr=list(map(int,input().strip().split()))
    solution(arr)