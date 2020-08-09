'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-08-01 15:25:33
@LastEditors: Liang Anqing
@LastEditTime: 2020-08-01 15:40:52
'''
def solution(money,n,value,cost):
    dp=[[]]
    for i in range(n):
        
if __name__=='__main__':
    money=int(input())
    n=int(input())
    value=[]
    cost=[]
    for i in range(n):
        cost.append(list(map(int,input().strip().split()[0])))
        value.append(list(map(int,input().strip().split()[1])))
    print(solution(money,n,value,cost))