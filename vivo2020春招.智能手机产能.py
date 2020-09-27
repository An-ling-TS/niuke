'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-09 13:29:48
LastEditors: Liang Anqing
LastEditTime: 2020-09-09 13:43:20
'''
'''

在vivo产线上，每位职工随着对手机加工流程认识的熟悉和经验的增加，日产量也会不断攀升。
假设第一天量产1台，接下来2天(即第二、三天)每天量产2件，接下来3天(即第四、五、六天)每天量产3件 ... ... 
以此类推，请编程计算出第n天总共可以量产的手机数量。




输入例子1:

11


输出例子1:

35


例子说明1:

第11天工人总共可以量产的手机数量

'''
def solution(n):
    #判断第n天产能为p  为满足p(p-1)/2<=n的最大值
    p=0
    for i in range(n):
        if i*(i-1)<=2*n and i*(i+1)>2*n:
            p=i
            break
    res=int(((p-1)*p*(2*p-1))/6)+int(n-(p*(p-1))/2)*p
    return res
if __name__=='__main__':
    n=int(input())
    print(solution(n))