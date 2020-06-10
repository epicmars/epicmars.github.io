#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def random_select(A, p, r, i):
    """
    A: 要查找的序列
    p: 序列开始索引，包含
    r: 序列结束索引，包含
    i: 要查找的顺序统计量
    """
    # 如果只有一个元素，直接返回
    if p == r:
        return A[p]
    q = random_partition(A, p, r)
    if i == q:
        return A[q]
    if i < q:
        return random_select(A, p, q-1, i)
    else:
        return random_select(A, q+1, r, i)
    
def random_partition(A, p, r):
    """
    A: 要划分的序列
    p: 序列开始索引，包含
    r: 序列结束索引，不包含
    """
    # 这里直接从中间进行划分
    mid = (p + r) / 2
    pivot = A[mid]  # 主元
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
    for i in xrange(0, len(A)-1):
        print random_select(A, 0, len(A)-1, i)

if __name__ == '__main__':
    main()