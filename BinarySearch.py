#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/9/17 15:03
# @Author : liaochao
# @File   : BinarySearch.py
# !/usr/bin/python
# @Description : 二分查找，主要用于在排好序的内容中查找
def binary_serarch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        # // 触发向下取整
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
           high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print (binary_serarch(my_list, 3))
print (binary_serarch(my_list, 0))

