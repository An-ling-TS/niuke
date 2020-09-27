'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-10 16:31:03
LastEditors: Liang Anqing
LastEditTime: 2020-09-10 17:11:00
'''
'''


有一个x*y*z的立方体，要在这个立方体上砍k刀，每一刀可以看作是用一个平行于立方体某一面的平面切割立方体，且必须在坐标为整数的位置切割，如在x=0.5处用平面切割是非法的。

问在切割k刀之后，最多可以把立方体切割成多少块。

输入描述:

输入仅包含一行，一行包含4个正整数x,y,z,k分别表示x*y*z的立方体和切割k刀。（1<=x,y,z<=10^6,0<=k<=10^9）


输出描述:

输出仅包含一个正整数，即至多切割成多少块。


输入例子1:

2 2 2 3


输出例子1:

8

'''
def solution(arr):
    border=arr[0:3]
    k=arr[3]
    #count存放每一边上的切割次数
    count={'0':0,'1':0,'2':0}
    for i in range(k):
        #选择长度大于1且已切割次数最小的边切割->保证乘积最大
        temp=[]
        for j in range(3):
            if border[j]>1:
                temp.append(str(j))
        if len(temp)==0:
            break
        min_pos=temp[0]
        for c in temp:
            if count[c]<count[min_pos] :
                min_pos=c
        count[min_pos]+=1
        border[int(min_pos)]-=1
    count=list(map(lambda x:x+1,count.values()))
    res=count[0]*count[1]*count[2]
    return res
if __name__=='__main__':
    arr=list(map(int,input().strip().split()))
    print(solution(arr))