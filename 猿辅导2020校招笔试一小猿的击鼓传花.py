'''


时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M
K(K>=3)个猿辅导的老师们在玩一个击鼓传花的小游戏。每击一次鼓，拿着花的老师要将花交给别人，不能留在自己手中。游戏开始前花在小猿手中，求击了N次鼓后，这朵花又回到小猿手中的方案数，请输出这个数模1000000007后的结果。

输入描述:

输入两个数N，K。

20%的数据：(3<=K<=10, 1<= N<=10)

70%的数据：(3<=K<=1000, 1<= N<=1000)

100%的数据：(3<=K<=10^9, 1<= N<=10^9)


输出描述:

输出方案数模1000000007后的结果


输入例子1:

3 3


输出例子1:

2

'''
'''
思路：
1.当n<=1时答案为0
2.假设小猿为A，则用长度为n+1且以A开头和结尾的字符串代表花从A出发最后传回A
3.将n+1长的字符串简化为不含A的字符串，长度为n-1
4.即求除了小猿以外的排列数
5.当n-1大于k-1时，res=（k-1全排列)^（（n-1）整除（k-1））*（（n-1）%（k-1）全排列）
'''
def getnum(n):
    if n==1 or n==0:
        return 1
    return n*getnum(n-1)
def solution(arr):
    n,k=arr
    if n<=1:
        return 0
    if n-1<=k-1:
        return int(int(getnum(k-1))//int(getnum(k-n)))%1000000007
    temp=getnum(k-1)
    yushu=(n-1)%(k-1)
    e=int(((n-1)-yushu)/(k-1))
    return pow(temp,e)*int(getnum(k-1)/int(getnum(k-1-yushu)))%1000000007
if __name__=='__main__':
    arr = list(map(int,input().strip().split()))
    print(int(solution(arr)))