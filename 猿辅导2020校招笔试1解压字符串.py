'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-16 16:29:56
LastEditors: Liang Anqing
LastEditTime: 2020-08-16 16:57:10
'''
'''

猿辅导APP需要下发一些宣传文本给学生，工程师们使用了一种字符压缩算法，为简单起见，假设被压缩的字符全部为大写字母序列，A,B,C,D....Z,压缩规则如下：
1.AAAB可以压缩为A3B (单字符压缩不加括号)
2.ABABA可以压缩为(AB)2A （多字符串压缩才加括号）

输入数据保证不会出现冗余括号，且表示重复的数字一定合法且大于1，即不会出现：
1.（A)2B   ------- （应为：A2B）
2.  ((AB))2C,-----(应为：（AB)2C  )
3. （A)B  ----- （应为：AB）
4.   A1B，（AB)1C，（应为 AB，ABC）

注意：数字可能出现多位数即A11B或者(AB)10C或者A02这种情况。
A11B = AAAAAAAAAAAB
(AB)10C = ABABABABABABABABABABC
A02 = AA

数据分布：
对于60%的数据，括号不会出现嵌套，即不会有 ((AB)2C)2这种结构。
对于80%的数据，括号最多只嵌套一层，即不会有 (((AB)2C)2D)99 这种结构。
对于100%的数据，括号可以嵌套任意层。

输入描述:

第一行是正整数C(C <= 100)，表示下面有C组数据。之后C行，每行为一组数据，每组数据为一个字符串。

每个字符串由A-Z,数字0-9和(,)组成表示一个压缩后的串，保证输入数据一定合法且字符串长度小于50。


输出描述:

输出C行，每行对应一个数据的输出结果，表示压缩前的字符串，保证每个字符串展开后的长度不超过10^6。


输入例子1:

5
A11B
(AA)2A
((A2B)2)2G
(YUANFUDAO)2JIAYOU
A2BC4D2


输出例子1:

AAAAAAAAAAAB
AAAAA
AABAABAABAABG
YUANFUDAOYUANFUDAOJIAYOU
AABCCCCDD

'''
def getRes(s):
    temp=[]
    res=''
    size=len(s)
    i=0
    while i <size:
        if s[i]>'9' or s[i]<'0':
            temp.insert(0,s[i])
            i+=1
            continue
        copy=''
        if len(temp)>0 and temp[0]==')':
            del temp[0]
        while len(temp)>0 and temp[0]!='(':
            copy+=temp[0]
            del temp[0]
        if len(temp)>0 and temp[0]=='(':
            del temp[0]
        copy=copy[::-1]
        count=0
        while s[i]<='9' and s[i]>='0':
            count+=count*10+int(s[i])
            i+=1
        for r in range(count):
            res+=copy
    for i in temp:
        res+=i
    return res
def solution(n,arr):
    res=[]
    for i in range(n):
        res.append(getRes(arr[i]))
    for i in range(n):
        print(res[i])
if __name__=='__main__':
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(input())
    solution(n,arr)