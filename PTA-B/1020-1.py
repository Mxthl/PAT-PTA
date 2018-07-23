#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n, d = map(int, raw_input().split())
lst1 = list(map(int, raw_input().split()))
lst2 = list(map(int, raw_input().split()))
dic = {}
for i in range(n):
    p = round(lst2[i]*1.0/lst1[i], 3)
    dic[i] = p
order = sorted(dic, key=lambda i: dic[i], reverse=True)
w = 0
for i in order:
    if d > lst1[i]:
        w += lst2[i]
        d -= lst1[i]
    else:
        w += d * dic[i]
        break
print '%.2f' % w


