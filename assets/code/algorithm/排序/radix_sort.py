#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def counting_sort_char(index, A, B, k):
    """
    i: the digit index for comparation
    """
    C = [0 for x in xrange(0, k+1)]
    for x in A:
        # digit index exceed digit length
        if index >= len(x):
            C[0] += 1
        else:
            C[ord(x[index])] += 1
    for i in xrange(0, k+1):
        if i > 0:
            C[i] += C[i-1]
    # Now C[i] contains the number of element smaller or equal to i,
    # which i is the digit of element of A whose index is "index"
    for j in xrange(len(A)-1, -1, -1):
        x = A[j]
        i = 0
        if index < len(x):
            i = ord(x[index])
        # index start with 0, so minus 1
        B[C[i]-1] = x
        C[i] -= 1

def radix_sort_string(A, d):
    size = len(A)
    for i in xrange(0, d):
        B = [None] * size
        counting_sort_char(i, A, B, 255)
        A = B
        print A
    return A

if __name__ == '__main__':
    A = ["a", "bc", "def", "c", "hello world", "asdasdf", "code", "python", "081324asdf", "1", "shark-"]
    d = 1
    for e in A:
        length = len(e)
        if length > d:
            d = length
    B = radix_sort_string(A, d)
    print B