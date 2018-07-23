C1, C2 = [int(i) for i in raw_input().split()]
CLK_TCK = 100
s = round((C2-C1)*1.0/CLK_TCK)
res_h = int(s/3600)
res_m = int(s%3600/60)
res_s = int(s) - res_h*3600 - res_m*60
res = '{:0>2d}'.format(res_h) + ':' + '{:0>2d}'.format(res_m) + ':' +'{:0>2d}'.format(res_s)
print res