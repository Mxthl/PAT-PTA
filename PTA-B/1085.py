#!/usr/bin/env python 
# -*- coding:utf-8 -*-

N = int(raw_input())
stu = {}
for n in range(N):
    num, sco, sch = [i for i in raw_input().split()]
    if sch.lower() not in stu:
        stu[sch.lower()] = {}
    stu[sch.lower()][num] = int(sco)
l = len(stu.keys())
res = {}
for k in stu.keys():
    zf = 0
    for xh, fs in stu[k].items():
        if xh[0] == 'B':
            zf += (fs*1.0)/1.5
        elif xh[0] == 'A':
            zf += fs
        else:
            zf += fs * 1.5
    res[k] = []
    res[k].append(int(zf))
    res[k].append(len(stu[k]))
result = sorted(res.items(),key=lambda x: (x[1][0]), reverse=True)


print l
for L in range(l):


