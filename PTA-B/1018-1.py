#!/usr/bin/env python 
# -*- coding:utf-8 -*-
if __name__ == '__main__':
    a = [0, 0, 0]
    b = [0, 0, 0]
    a1 = 0
    b1 = 0
    lst_s = ['B', 'C', 'J']
    n = int(raw_input())
    for i in range(n):
        s1, s2 = raw_input().split()
        if s1 == 'C' and s2 == 'J':
            a[1] += 1
            a1 += 1
        elif s1 == 'J' and s2 == 'B':
            a[2] += 1
            a1 += 1
        elif s1 == 'B' and s2 == 'C':
            a[0] += 1
            a1 += 1
        elif s2 == 'C' and s1 == 'J':
            b[1] += 1
            b1 += 1
        elif s2 == 'J' and s1 == 'B':
            b[2] += 1
            b1 += 1
        elif s2 == 'B' and s1 == 'C':
            b[0] += 1
            b1 += 1
    print a1, n-a1-b1, b1
    print b1, n-a1-b1, a1
    print lst_s[a.index(max(a))], lst_s[b.index(max(b))]