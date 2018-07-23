#!/usr/bin/env python 
# -*- coding:utf-8 -*-
if __name__ == '__main__':
    s1 = raw_input()
    s2 = raw_input()
    day_dic = {'A': 'MON', 'B': 'TUE', 'C': 'WED', 'D': 'THU', 'E': 'FRI', 'F': 'SAT', 'G': 'SUN'}
    lst = []
    s = ''
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i] and s1[i].isupper():
            if s == '':
                s += day_dic[s1[i]]
            else:
                if s1[i].isupper():
                    s = s + ' ' + str(ord(s1[i]) -55)
                else:
                    s = s + ' ' + '0' + s1[i]

    s3 = raw_input()
    s4 = raw_input()
    for i in range(min(len(s3), len(s4))):
        if s3[i] == s4[i] and s3[i].isalpha():
            if i < 10:
                s = s + ':' + '0' + str(i)
            else:
                s = s + ':' + '0' + str(i)

    print s

