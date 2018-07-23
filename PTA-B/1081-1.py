#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def is_legal(s):
    zimu = []
    shuzi = []
    dian = []
    if len(s) < 6:
        print 'Your password is tai duan le.'
    else:
        for i in s:
            if i.isalpha():
                zimu.append(i)
            elif i.isdigit():
                shuzi.append(i)
            elif i == '.':
                dian.append(i)
        if len(zimu) + len(shuzi) + len(dian) == len(s):
            if len(shuzi) == 0:
                print 'Your password needs shu zi.'
            elif len(zimu) == 0:
                print 'Your password needs zi mu.'
            else:
                print 'Your password is wan mei.'
        else:
            print 'Your password is tai luan le.'
    return
if __name__ == '__main__':
    n = input()
    for c in range(n):
        pw = raw_input()
        is_legal(pw)