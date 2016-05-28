#!/bin/python

import sys


n = int(raw_input().strip())
b_n = bin(n)
cnt = 0
tem_cnt = 0
cnt_conti = False

for key in b_n:    
    if key == '1':       
        if cnt_conti == True:
            tem_cnt = tem_cnt +1
            
        else:
            tem_cnt = 1
            
        cnt_conti = True
        if tem_cnt > cnt:
            cnt = tem_cnt


    else :
        cnt_conti = False
        tem_cnt = 0
print cnt