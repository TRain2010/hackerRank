#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
max_sum = arr[0][0] + arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0] + arr[2][1]+arr[2][2]
tem_sum = 0
for i in range(0,4):
    for j in range(0,4):
        tem_sum = tem_sum+arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        if tem_sum > max_sum:
            max_sum = tem_sum
        tem_sum = 0
    
print max_sum