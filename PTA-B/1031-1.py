#!/usr/bin/env python 
# -*- coding:utf-8 -*-
if __name__ == '__main__':
    n = [int(x) for x in raw_input().split()]
    num = 0
    now = 2
    while num < n[1]:
        dec = 1
        for i in range(int(now**0.5)+1):
            if i > 1 and i < now:
                if now % i == 0:
                    dec = 0
                    break
        if dec == 1 and num+1 >= n[0]:
            if (num+2-n[0]) % 10 != 0:
                if num+1 == n[1]:
                    print now
                else:
                    print now,
            else:
                print now
        if dec == 1:
            num += 1
        now += 1