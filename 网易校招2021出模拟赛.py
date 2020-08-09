'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-08 15:18:53
LastEditors: Liang Anqing
LastEditTime: 2020-08-08 15:48:28
'''
'''
思路：
1.初始化E_t，M_t，H_t分别为E，EM+MH+M，H
2.循环：
    取E_t，H_t较小值+1，对应MH或EM-1 如果EM HM不足则退出循环
    更新E_t，M_t，H_t
    如果E_t>=M_t and H_t>=M_t则退出循环
3.返回结果
'''
def solution(arr):
    res=0
    E,EM,M,MH,H=arr
    while True:
        E_t=E
        M_t=EM+MH+M
        H_t=H
        if E_t>=M_t and H_t>=M_t:
            res=M_t
            break
        min_=min(E_t,H_t)
        if min_==E_t:
            if EM>0:
                EM-=1
                E+=1
            else:
                res=min_
                break
        else:
            if MH>0:
                MH-=1
                H+=1
            else:
                res=min_
                break
    return res
if __name__=='__main__':
    
    while True:
        arr=list(map(int,input().strip().split()))
        print(solution(arr))