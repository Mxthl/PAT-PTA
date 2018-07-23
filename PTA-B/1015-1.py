#!/usr/bin/env python 
# -*- coding:utf-8 -*-
if __name__ == '__main__':
    def ranking(x):
        sum = -x[1] - x[2]
        a = -x[1]
        b = x[0]
        return sum, a, b

    n, low, high = list(map(int, raw_input().split()))
    l1, l2, l3, l4, bad = [], [], [], [], 0
    for row in range(n):
        i = list(map(int, raw_input().split()))
        if i[1]<low or i[2]<low:
            bad += 1
        else:
            if i[1]>=high:
                if i[2]>=high:
                    l1.append(i)
                else:
                    l2.append(i)
            else:
                if i[2]<=i[1]:
                    l3.append(i)
                else:
                    l4.append(i)
    print n-bad
    for l in (l1, l2, l3, l4):
        l.sort(key=ranking)
        for i in l:
            print i[0], i[1], i[2]