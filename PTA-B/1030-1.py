#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n, p = [int(i) for i in raw_input().split()]
lst = [int(s) for s in raw_input().split()]
lst.sort()
m = 0
for i in range(n):
    m_q = lst[i] * p
    next_ = i + m
    if next_ >= n:
        break
    for j in range(next_, n):
        if lst[j] <= m_q:
            m += 1
        else:
            break

print m