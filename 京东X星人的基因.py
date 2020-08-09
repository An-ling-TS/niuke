'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-08-06 19:38:13
@LastEditors: Liang Anqing
@LastEditTime: 2020-08-06 19:57:59
'''
def solution(n,p_1,p_2):
    dp=1 if p_1[0]==p_2[0] else 0
    temp=0
    for i in range(1,n):
        if p_2[i] in p_1[temp+1:i+1]:
            temp=p_1.index(p_2[i])
            dp+=1
            if temp==n-1:
                break
    res=round(dp/n,2)
    ans=' Yes' if res<0.5 else ' No'
    print(str(res)+ans)
if __name__=='__main__':
    n=int(input())
    p_1=list(input().strip().split())
    p_2=list(input().strip().split())
    solution(n,p_1,p_2)
    