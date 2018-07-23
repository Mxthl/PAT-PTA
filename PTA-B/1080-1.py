#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def is_pass(dic):
    res = {}
    for k, v in dic.items():
        if 'qz' not in v:
            v['qz'] = -1
        if v['qz'] > v['qm']:
            g = v['qz'] * 0.4 + v['qm'] * 0.6
        else:
            g = v['qm']
        if g >= 60:
            res[k] = [v['bc'], v['qz'], v['qm'], int(round(g))]
    ord_res = sorted(res.items(), key=lambda x: (x[1][3], -ord(x[0][0])), reverse=True)
    for a1, [b1, b2, b3, b4] in ord_res:
        print a1, b1, b2, b3, b4
    return

if __name__ == '__main__':
    p, m, n = [int(p) for p in raw_input().split()]
    dic = {}
    for i1 in range(p):
        xh1, f1 = raw_input().split()
        if int(f1) >= 200:
            if xh1 not in dic:
                dic[xh1] = {}
            dic[xh1]['bc'] = int(f1)
    for i2 in range(m):
        xh2, f2 = raw_input().split()
        if xh2 in dic:
            dic[xh2]['qz'] = int(f2)
    for i3 in range(n):
        xh3, f3 = raw_input().split()
        if xh3 in dic:
            dic[xh3]['qm'] = int(f3)

    is_pass(dic)



