#coding=utf-8

import time

now = time.time()


def findSmallest(arr):
    """选择排序，找到最小元素"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """选择排序，对数组进行排序"""
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 2, 10]))
    print(time.time() - now)