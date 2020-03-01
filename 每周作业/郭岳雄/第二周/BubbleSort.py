#!/usr/bin/env python

# -*- encoding: utf-8 -*-
# Python37-32
'''
@Author  :   {Gavin Guo}
@License :   (C) Copyright 2019-2024, {XXX's Company}
@Contact :   {878953027@qq.com}
@Software:   PyCharm
@File    :   BubbleSort.py
@Time    :   2020/2/28 16:58
@Desc    :
'''

'''
冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。
它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果顺序（如从大到小、首字母从Z到A）错误就把他们交换过来。走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端（升序或降序排列），就如同碳酸饮料中二氧化碳的气泡最终会上浮到顶端一样，故名“冒泡排序”。
'''

def BubbleSort(sortlist):

    for i in range(len(sortlist)-1):

        for j in range(len(sortlist)-1):
            bak = sortlist[j]
            if sortlist[j] < sortlist[j+1]:
                sortlist[j] = sortlist[j+1]
                sortlist[j+1] = bak


# Test code
sortlist = [1, 27, 2, 43, 8, 98]
#befor sort
print(sortlist)
BubbleSort(sortlist)
#after sort
print(sortlist)

