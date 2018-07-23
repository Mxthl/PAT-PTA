#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n = raw_input()
e = n.index('E')
d0 = 0
for d in n[0:e]:
    if d == '0':
        d0 += 1
    else:
        d0 = 0
s1 = float(n[0:e])
s2 = int(n[e+1:])
r = s1*10**s2
if r == round(r):
    print int(r)
else:
    r = str(r) + '0'*d0
    print r