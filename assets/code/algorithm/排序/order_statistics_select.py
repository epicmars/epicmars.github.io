#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def insertion_sort(A, r):
    for i in xrange(0, len(r)):
        current = i
        for j in xrange(i, -1, -1):
            if A[r[current]] < A[r[j]]:
               swap(A, r[current], r[j])
               current = j

def median(A, r):
    # print "median", r
    insertion_sort(A, r)
    if len(r) % 2 == 1:
        return r[len(r) / 2]
    else:
        return r[len(r) / 2 - 1]

def select(A, r, i):
    # print "select", r
    """
    A: 要查找顺序统计量的序列
    r: 查找的序号
    """
    size = len(r)
    if size == 1:
        return r[0]
    start = r[0]      # start index in A
    end = r[size - 1] # end index in A
    medians = []
    if size % 5 == 0:
        num = size / 5
    else:
        num = size / 5 + 1
    for j in xrange(0, num):
        s = j * 5    # start index of r
        e = s + 5    # end index of r
        if e >= size:
            e = size
        m = median(A, r[s : e])
        medians.append(m)
    x = select(A, medians, i)
    k = partition(A, x, start, end)
    # print "after partition", i, k, x, start, end
    if i == k:
        return x
    elif i < k and k > start:
        return select(A, range(start, k), i)
    else:
        return select(A, range(k+1, end+1), i)

def partition(A, x, p, r):
    # print "partition", x, p, r
    pivot = A[x]
    left = p        # [p,left)间的元素都小于等于主元
    right = r       # (right,r]间的元素都大于等于主元
    while left < right:
        if A[left] >= pivot and A[right] <= pivot: 
            swap(A, left, right)
            left += 1
            right -= 1
        else:
            if A[left] < pivot:
                left += 1
            if A[right] > pivot:
                right -= 1
    return left


def main():
    A = [100, 134, -1, 1324, 1123, 9, 34, 3, -98, 132, 3, 3, 12, 29, 36]
    for i in xrange(0, len(A)):
        print A[select(A, range(0, len(A)), i)]

if __name__ == '__main__':
    main()