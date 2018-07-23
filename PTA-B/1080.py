#!/usr/bin/env python 
# -*- coding:utf-8 -*-
P, M, N = [int(p) for p in raw_input().split()]
sco = {}
for p_ in range(P):
    num1, gp = [n1 for n1 in raw_input().split()]
    sco[num1] = {}
    sco[num1]['gp'] = int(gp)

for m in range(M):
    num2, gm = [n2 for n2 in raw_input().split()]
    if num2 not in sco.keys():
        sco[num2] = {}
        sco[num2]['gp'] = -1
        sco[num2]['gm'] = int(gm)
    else:
        sco[num2]['gm'] = int(gm)

for n in range(N):
    num3, gf = [n3 for n3 in raw_input().split()]
    if num3 not in sco.keys():
        sco[num3] = {}
        sco[num3]['gp'] = -1
        sco[num3]['gm'] = -1
        sco[num3]['gf'] = int(gf)
    else:
        sco[num3]['gf'] = int(gf)

