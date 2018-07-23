#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n, s = raw_input().split()
i = 0
while 2*i**2 - 1 < int(n):
    i += 1
d = int(n) - 2 * (i-1)**2 + 1
s1 = 2 * i - 3
b = 0
while s1 > 0:
    print b *' ' + s1 * s + b * ' '
    s1 -= 2
    b += 1
for c in range(1, b):
    print c*' ' + (2*c+1) * s + c * ' '
print d



