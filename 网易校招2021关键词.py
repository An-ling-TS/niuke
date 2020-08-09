'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-08 15:04:22
LastEditors: Liang Anqing
LastEditTime: 2020-08-08 15:14:49
'''
def solution(n,arr):
    words=dict()
    res=0
    temp=n*0.01
    for word in arr:
        if word in words.keys():
            if words[word]>-1:
                words[word]+=1
        else:
            words[word]=1
        if words[word]>-1:
            if words[word]>=temp:
                words[word]=-1
                res+=1
    return res

if __name__=='__main__':
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(input())
    print(solution(n,arr))