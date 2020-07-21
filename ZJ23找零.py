'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-13 14:52:57
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-13 14:53:24
'''
def solution(n):
    rs=0
    temp=1024-n
    rs+=int(temp/64)
    temp=temp%64
    rs+=int(temp/16)
    temp=temp%16
    rs+=int(temp/4)+temp%4
    return rs
if __name__=='__main__':
    n=int(input())
    print(solution(n))