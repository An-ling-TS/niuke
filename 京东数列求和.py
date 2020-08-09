'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-08-06 19:23:58
@LastEditors: Liang Anqing
@LastEditTime: 2020-08-06 19:36:40
'''
def solution(n):
    rs=0
    flag=1
    for i in range(1,2*n+1):
        rs+=(1/i)*flag
        flag*=-1
    rs*=0.2000
    return round(rs,4)
if __name__=='__main__':
    n=int(input())
    res=solution(n)
    print(res)