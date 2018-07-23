#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n = input()
d = {}
for i in range(n):
    s1, s2, s3 = raw_input().split()
    s4 = s3.lower()
    if s4 not in d:
        d[s4] = []
    if s1[0] == 'B':
        f = int(s2)/1.5
    elif s1[0] == 'A':
        f = int(s2)
    elif s1[0] == 'T':
        f = int(s2)*1.5
    d[s4].append(f)
res = {}
for k in d.keys():
    c = int(sum(d[k]))
    l = len(d[k])
    res[k] = [c, l]

order1 = sorted(res.items(), key=lambda x: (x[1][0], -x[1][1], -ord(x[0][0])), reverse=True)
order2 = sorted([o[1][0] for o in order1], reverse=True)

print len(res)
for k, [v1, v2] in order1:
    print order2.index(v1), k, v1, v2


