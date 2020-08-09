'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-23 15:02:22
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-23 15:16:55
'''
def solution(n,a,b):
    res=0
    for i in range(n):
        for j in range(n):
            print('i='+str(i))
            print('j='+str(j))
            if b[i]==a[j]:
                res+=1
                del b[i]
                del a[j]
                
                i-=1
                j-=1
                break
    if len(b)==0:
        if len(a)>0:
            return res
        return res-1
    if len(a)>0:
        return res+1
    return res
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().strip().split()))
    b=list(map(int,input().strip().split()))
    print(solution(n,a,b))