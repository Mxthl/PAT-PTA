#!/usr/bin/env python 
# -*- coding:utf-8 -*-
poly = [int(p) for p in raw_input().split()]
if poly[-1] == 0:
    del poly[-2:]

if poly:
    poly_l = list(range(len(poly)))
    for i, p in enumerate(poly):
        if i % 2 == 0:
            poly_l[i] = str(p*poly[i+1])
            poly_l[i+1] = str(poly[i+1] - 1)

else:
    poly_l = '00'

print (' '.join(poly_l).strip())