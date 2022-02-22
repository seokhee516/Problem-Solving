'''
N   return 
1   1
2   00 11
3   111 (N=1) 100 001 (N=2) 
4   0000 0011 (N=2)
    1111 1100 1001 (N=3)
5   00111 00100 00001 (N=3)
    10000 10011
    11111 11100 11001 (N=4)
...

N = N-1 + N-2
'''

import sys
N = int(sys.stdin.readline())
d = [0] * 1000001 # 10^6보다 작거나 같은 정수 N 자리 만들어줌
d[1] = 1
d[2] = 2
for i in range(3,N+1):
    d[i] = (d[i-1] + d[i-2])%15746 # 15746으로 나눈 나머지
print(d[N])