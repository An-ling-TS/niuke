'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-09 12:35:07
LastEditors: Liang Anqing
LastEditTime: 2020-09-09 13:26:45
'''
'''
现给定任意正整数 n，请寻找并输出最小的正整数 m（m>9），使得 m 的各位（个位、十位、百位 ... ...）之乘积等于n，若不存在则输出 -1。

输入例子1:

36


输出例子1:

49


输入例子2:

100


输出例子2:

455

'''
def solution(n):
    #n只有一位时，m=10+n
    if n<10:
        print(10+n)
        return 10+n
    
    #质因数分解
    factors=[]
    temp=n
    while temp!=1:
        for i in range(2,int(temp+1)):
            if temp%i==0:
                temp=temp/i
                factors.append(i)
                break
    #得到从小到大的有序质因数列表
    
    #质因数存在大于7时，不存在m
    if factors[len(factors)-1]>7:
        print(-1)
        return -1

    #列表值合并
    #循环:从右向左合并
    #循环条件 i>0
        #循环:原地循环
        #循环条件 factors[i]*factors[i-1]<10
            #factors[i]*=factors[i-1]
            #del factors[i-1]
            #i--
        #循环结束
        #i-=1
    #循环结束
    i=len(factors)-1
    while i>0:
        while factors[i]*factors[i-1]<10:
            factors[i]*=factors[i-1]
            factors.pop(i-1)
            i-=1
        i-=1
    factors=sorted(factors)
    res=''
    for i in range(len(factors)):
        res+=str(factors[i])
    print(int(res))
    return int(res)
if __name__=='__main__':
    n=int(input())
    solution(n)