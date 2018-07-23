#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n = input()
ls1 = []
ls2 = []
for i in range(n):
    s1, s2 = [int(s) for s in raw_input().split()]
    if s1 not in ls1:
        ls1.append(s1)
        ls2.append(s2)
    else:
        ls2[ls1.index(s1)] += s2

r1 = max(ls2)
print ls1[ls2.index(r1)], r1
