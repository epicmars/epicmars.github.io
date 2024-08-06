#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def merge_sort(A, start, end):
    if end - start <= 1:
        return
    mid = (end + start) / 2
    merge_sort(A, start, mid)
    merge_sort(A, mid, end)
    merge(A, start, mid, end)

def merge(A, start, mid, end):
    left = []
    right = []
    for i in xrange(start, mid):
        left.append(A[i])
    for i in xrange(mid, end):
        right.append(A[i])
    i = 0
    j = 0
    current = start
    left_size = len(left)
    while i < left_size and j < len(right):
        if left[i] <= right[j]:
            A[current] = left[i]
            i += 1
        else:
            A[current] = right[j]
            j += 1
        current += 1
    for k in xrange(i, left_size):
        A[current] = left[k]
        current += 1

if __name__ == '__main__':
    A = [12, 12, 123, 234, 1, 2, 3, 4000, 12, 234, 1, 891]
    merge_sort(A, 0, len(A))
    print A