#!/usr/bin/env python 
# -*- coding:utf-8 -*-
if __name__ == '__main__':

    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []

    lst = [int(l) for l in raw_input().split()]
    for i in range(lst[0]):
        if lst[i+1] % 10 == 0:
            a1.append(lst[i+1])
        elif lst[i+1] % 5 == 1:
            a2.append(lst[i+1])
        elif lst[i+1] % 5 == 2:
            a3.append(lst[i+1])
        elif lst[i+1] % 5 == 3:
            a4.append(lst[i+1])
        elif lst[i+1] % 5 == 4:
            a5.append(lst[i+1])

    if a1:
        print sum(a1),
    else:
        print 'N',
    if a2:
        a2_ans = 0
        for i in range(len(a2)):
            if i % 2== 0:
                a2_ans += a2[i]
            else:
                a2_ans -= a2[i]
        print a2_ans,
    else:
        print 'N',

    if a3:
        print len(a3),
    else:
        print 'N',
    if a4:
        print round((sum(a4)*1.0/len(a4)), 1),
    else:
        print 'N',
    if a5:
        print max(a5)
    else:
        print 'N'
