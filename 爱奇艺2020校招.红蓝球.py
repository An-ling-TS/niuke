'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-10 18:57:48
LastEditors: Liang Anqing
LastEditTime: 2020-09-10 19:20:01
'''
'''


有一个非常经典的概率问题，是一个袋子里面有若干个红球和若干个蓝球，两个人轮流取出一个球，谁先取到红球谁就赢了，当人的先后顺序和球的数量确定时，双方的胜率都可以由计算得到，这个问题显然是很简单的。

现在有一个进阶版的问题，同样是一个袋子里面有n个红球和m个蓝球，共有A，B，C三人参与游戏，三人按照A，B，C的顺序轮流操作，在每一回合中，A，B，C都会随机从袋子里面拿走一个球，然而真正分出胜负的只有A，B两个人，没错，C就是来捣乱的，他除了可以使得袋子里面减少一个球，没有其他任何意义，而A，B谁 先拿到红球就可以获得胜利，但是由于C的存在，两人可能都拿不到红球，此时B获得胜利。

输入描述:

输入仅包含两个整数n和m,表示红球和蓝球的数量，中间用空格隔开。(0<=n,m<=1000)


输出描述:

请你输出A获胜的概率，结果保留5位小数。


输入例子1:

1 1


输出例子1:

0.50000


输入例子2:

3 4


输出例子2:

0.62857

'''
def solution(arr):
    n,m=arr
    #至多在第t轮决出胜负,最开始为第0轮
    t=int((m-m%3)/3)
    Pa=[]
    Sa=[]
    Sb=[]
    Sc=[]
    Pc=[]
    for i in range(t):
        if i==0:
            #Pai为A在第i轮胜利概率，Sa为在此轮拿蓝球概率
            Pa.append(n/(n+m))
            Sa.append(m/(n+m))
            Sb.append((m-1)/(n+m-1))
            Sc.append((m-2)/(n+m-2))
            Pc.append(n/(n+m-2))
            continue
        #当i>0时，A胜率Pa[i]=Sa[i-1]*Sb[i-1]*Sc[i-1]*
if __name__=='__main__':
    arr=list(map(int,input().strip().split()))
    print(solution(arr))