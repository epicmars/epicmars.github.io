#!/usr/bin/env python
# -*- UTF-8 -*-

def counting_sort_integer(A, B, k):
    C = [0 for x in xrange(0, k+1)]
    for x in A:
        C[x] += 1
    for i in xrange(0, k+1):
        if i > 0:
            C[i] += C[i-1]
    for x in A:
        B[C[x]-1] = x
        C[x] -= 1

if __name__ == '__main__':
    A = [123, 21, 14321, 0, 120, 98, 1000, 1024, 123, 1, 0, 123, 24, 123, 3, 2, 12]
    B = [None] * len(A)
    counting_sort_integer(A, B, 14321)
    print B