#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import math

def is_prime(num):
    i = 2
    cnt = int(math.sqrt(num))
    while i <= cnt:
        if num % i == 0:
            return False
        i += 1

    return True

if __name__ == '__main__':
    n = input()
    prev = i = 2
    cnt = 0
    while i <= n:
        if is_prime(i):
            if i - prev == 2:
                cnt += 1
            prev = i
        i += 1
    print cnt