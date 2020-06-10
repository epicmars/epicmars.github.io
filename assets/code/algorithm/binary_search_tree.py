#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Node(object):
    """
    A node of a binary search tree, it has a key as data,
    a parent node, a left child node, a right child node,
    these node can be NIL, a NIL parent node means root
    of the tree.
    """
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

class BinaryTree(object):
    """
    A binary tree use a linked list to store it's nodes.
    """
    def __init__(self):
        self.root = None

    