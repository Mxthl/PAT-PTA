#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n = input()
dic = {}
t = [2014, 9, 6]
for i in range(n):
    s1, s2 = raw_input().split()
    temp = [c for c in s2.split('/')]
    d1 = ''
    for d in temp:
        d1 += d
    if int(d1) >= 18140906 and int(d1) <= 20140906:
        age = (int(temp[0])-t[0])*365 +(int(temp[1])-t[1])*30+(int(temp[2])-t[2])
        dic[s1] = age
res = sorted(dic.items(), key=lambda x: x[1])
print len(res), res[0][0], res[-1][0]

