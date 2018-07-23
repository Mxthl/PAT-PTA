#!/usr/bin/env python 
# -*- coding:utf-8 -*-
N = int(raw_input())
def is_palin(number):
    n = str(number)
    m = n[::-1]
    return m == n
if (is_palin(N)):
    print '%s is a palindromic number' % N
else:
    res = 1
    temp = N
    n_n = int(str(temp)[::-1])
    s = temp + n_n
    for i in range(10):
        print '%s + %s = %s' %(temp, n_n, s)
        if is_palin(s):
            res = 0
            print '%s is a palindromic number.' %(n_n + temp)
            break
        else:
            temp = s
            n_n = int(str(temp)[::-1])
            s = temp + n_n
if res:
    print 'Not found in 10 iterations.'