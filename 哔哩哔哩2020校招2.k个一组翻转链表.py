'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-08 13:09:47
LastEditors: Liang Anqing
LastEditTime: 2020-09-08 13:34:20
'''
'''
[编程题]k个一组翻转链表

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M
给你一个链表，每 k 个节点一组进行翻转，请返回翻转后的链表。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5


输入描述:

第一行：依次输入链表中的各个元素，以"#"结束

第二行：每组数量k


输出描述:

处理后的链表中的各个元素，以"->"连接


输入例子1:

1 2 3 4 5 #
2


输出例子1:

2->1->4->3->5


输入例子2:

1 2 3 4 5 #
3


输出例子2:

3->2->1->4->5

'''
def solution(s,k):
    li=list(map(int,s.replace('#','').strip().split(' ')))
    count=int(len(li)/k)
    rs=''
    for i in range(count):
        temp=li[i*k:(i+1)*k]
        temp.reverse()
        for i in range(k):
            rs+='->'+str(temp[i])
    for i in range(count*k,len(li)):
        rs+='->'+str(li[i])
    rs=rs.replace('->','',1)
    print(rs)
if __name__=='__main__':
    s=input()
    k=int(input())
    solution(s,k)