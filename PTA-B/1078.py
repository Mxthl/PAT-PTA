#!/usr/bin/env python 
# -*- coding:utf-8 -*-
J = raw_input()
inp = [i for i in raw_input().split()]
def ys(data):
    result = ''
    pattern = data[0]
    count = 1
    for d in data[1:]:
        if d == pattern:
            count += 1
        else:
            if count == 1:
                result += pattern
                pattern = d
            else:
                result += (str(count) + pattern)
                pattern = d
                count = 1
    print result,
    return
def jy(data):
    return
if J == 'C':
    for temp in inp:
        ys(temp)
else:
    for temp in inp:
        jy(temp)




