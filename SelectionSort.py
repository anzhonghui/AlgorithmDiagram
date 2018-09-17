#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/17 17:15
# @Author : liaochao
# @File   : SelectionSort.py
# @Description : 选择排序

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        # append 向数组中追加元素；pop 从数组中拿出元素
        newArr.append(arr.pop(smallest_index))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
