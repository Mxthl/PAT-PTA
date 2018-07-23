#!/usr/bin/env python 
# -*- coding:utf-8 -*-

n = input()
nums = set()
outer = set()
x = map(int, raw_input().split())
for i in x:
    outer.add(i)
    while i != 1:
        if i in nums:
            if i in outer:
                outer.remove(i)
            break
        else:
            nums.add(i)

        if i%2 == 0:
            i /= 2
        else:
            i = (i*3+1)/2
s = [i for i in outer]
s.sort(reverse=True)
for i in s:
    print i,