#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def number(N):
    if int(N)>0 and int(N)<10000:
        if 0<int(N)<10:
            N='000' + N
        elif 10<=int(N)<100:
            N='00' + N
        elif 100<=int(N)<1000:
            N='0' + N
        else:
            N=N
    return N

def operation(N):
    N = number(N)
    while True:
        L = []
        for i in range(len(N)):
            L.append(N[i])
            L.sort(reverse=True)
            n1 = ''.join(L)
            L.sort()
            n2 = ''.join(L)
        if int(n1) == int(n2):
            print '%s - %s = 0000' %(n1, n2)
            break
        result = int(n1) - int(n2)
        if result<1000:
            result = '0' + str(result)
        print '%s - %s = %s' %(n1, n2, result)
        if result != 6174:
            N=str(result)
            continue
        else:
            break

if __name__ == '__main__':
    N = raw_input()
    operation(N)



