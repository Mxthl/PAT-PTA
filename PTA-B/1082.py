#!/usr/bin/env python 
# -*- coding:utf-8 -*-
N = int(raw_input())
res = {}
for n in range(N):
    num, x, y = [i for i in raw_input().split()]
    s = int(x)**2 + int(y)**2
    res[num] = s
ans = []
ans.append(sorted(res.items(), key=lambda x: x[1])[0])
ans.append(sorted(res.items(), key=lambda x: x[1])[-1])
for k,v in ans:
    print k,