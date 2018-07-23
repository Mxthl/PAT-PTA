#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import re
if __name__ == '__main__':
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(raw_input())

    for st in lst:

        pa = re.compile(r'(?P<a>A*)P(?P<b>A+)T(?P<c>A*)')

        if pa.match(st):
            co = re.split(r'P|T', st)
            if len(co[0]) * len(co[1]) == len(co[2]):
                print 'YES'
            else:
                print 'NO'
        else:
            print 'NO'