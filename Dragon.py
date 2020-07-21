'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-19 20:44:04
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-19 21:19:55
'''
'''
链接：https://ac.nowcoder.com/acm/problem/14334
来源：牛客网

题目描述
《轩辕剑外传：苍之涛》是大宇资讯旗下经典单机角色扮演游戏《轩辕剑》系列的第七部作品。
这是《轩辕剑》系列中Roth最喜欢的一部作品,主要的原因是这部作品中引入了"法宝"系统，游戏中玩家可以装备两件类型为"法宝"的装备，每种法宝可以在战斗中为装备者提供技能，并且法宝可以成长，成长之后技能将更加强力。
而在苍之涛中，Roth最喜欢的一个法宝叫做"...龙...",这个法宝的技能是对一个敌人造成随机伤害.随机的伤害值分为3位，每一位为一个0-9之间的数字，每个数字由玩家在旋转的轮盘中点击鼠标发出停止指令时指针悬停的数字位置确定，升级之后伤害值将变为4位,并且可以组织数字的位置.Roth在游戏的过程中经常用"...龙..."对敌人造成成吨的输出,现在请你帮助Roth确定对于已经选定好的4位数字，他可以造成的最大伤害是多少
输入描述:

每组数据包含4个整数a,b,c,d；
0<=a,b,c,d<=9;
处理到文件尾

输出描述:

输出可能的最大的伤害值（不要包含前导0）

示例1
输入
复制

2 0 4 8
0 0 0 0
0 0 4 0

输出
复制

8420
0
4000
'''
'''
牛客的输入输出是真恶心，就不能像LeetCode一样吗，这丫的是靠算法还是考输入输出的
'''
def solution(arr):
    res=0
    while len(arr)>0:
        res=res*10+max(arr)
        del arr[arr.index(max(arr))]
    return res
if __name__=='__main__':
    res=[]
    while True:
        try:
            arr=list(map(int,input().strip().split()))
            print(solution(arr))
        except:
            break
    