'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-14 14:53:46
LastEditors: Liang Anqing
LastEditTime: 2020-08-14 15:21:29
'''
'''
def getMaxCom(a,b):
    for i in range(a>>1,1,-1):
        if a%i==0 and b%i==0 and a>i:
            return i
    return -1
def solution(arr):
    n,m=arr
    res=0
    while n<m:
        temp=getMaxCom(n,m)
        if temp==-1:
            return -1
        n+=temp
        res+=1
    return res
if __name__=='__main__':
    arr=list(map(int,input().strip().split()))
    print(solution(arr))
    '''
import sys
import collections

def jump(N, M):
    divs = [[] for _ in range(M+1)]
    for i in range(2, M+1):
        for j in range(i+i, M+1, i):
            divs[j].append(i)
    res = [0]*(M+1)
    res[N] = 1
    for n in range(N, M):
        if res[n]:
            for dn in divs[n]:
                if n + dn <= M:
                    res[n+dn] = min(res[n+dn], res[n] + 1) if res[n+dn] else res[n] + 1
    return res[M]-1 if res[M] else -1

if __name__ == '__main__':
    try:
        std_in = sys.stdin
##        std_in = open("parlindromes.txt")
        while True:
            line = std_in.readline()
            if line == '':
                break
            line = [int(t) for t in line.splitlines()[0].split()]
            print(jump(line[0], line[1]))
    except:
        pass
