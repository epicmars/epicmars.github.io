#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubble_sort(A):
    for i in xrange(len(A) - 1, -1, -1):
        max = A[i]
        for j in xrange(i - 1, -1, -1):
            if A[j] > max:
                max = A[j]
                swap(A, i, j)

def bucket_sort(A):
    n = len(A)
    min_v = min(A)
    max_v = max(A)
    range = max_v - min_v
    range += range / n
    bucket = [[] for _ in xrange(0, n)]
    for x in A:
        i = int((x - min_v) / range * n)
        bucket[i].append(x)
    current = 0
    for i in xrange(0, n):
        bubble_sort(bucket[i])
        for x in bucket[i]:
            A[current] = x
            current += 1

if __name__ == '__main__':
    A = [57, 35, -100.2, -12, -20, -23.123, 0, -12, -20, -23.123, 0, 1, 23, 214, 123, 135]
    bucket_sort(A)
    print A

