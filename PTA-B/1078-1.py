#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def jieya(s):
    res = ''
    for i in range(0,len(s),2):
        if s[i].isalpha():
            s.insert(i, 1)
        res += int(s[i]) * s[i+1]
    for r in res:
        print r,
    return

def yasuo(s):
    for s1 in s:
        temp = ''
        for i in s1:




    return

if __name__ == '__main__':
    flag = raw_input()
    s = list(raw_input())
    if flag == 'C':
        yasuo(s)
    else:
        jieya(s)
