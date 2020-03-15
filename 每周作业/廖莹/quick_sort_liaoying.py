def Partition(L,left,right):
    #确定比较子
    pivotkey=L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        #当小于比较子时，将其放到左边
        L[left]=L[right]
        while left < right and L[left] <=pivotkey:
            left += 1
        #当大于比较子时，将其放到右边
        L[right]=L[left]
    # 将比较子放到区间中
    L[left]=pivotkey
    #返回pivotkey排序后的下标
    return left

#递归方式调用（自己调用自己）
def quick_sort(L,left,right):
    #确定终止条件：
    if left < right :
        #调用分区函数，确定区间的分段下标值，进行第一次分区
        pivot=Partition(L,left,right)

        #分区后，小于的区间进行递归调用(自己调用自己才是递归调用）
        quick_sort(L,left,pivot-1)

        #分区后，大于的区间进行递归调用
        quick_sort(L,pivot+1,right)
    #不满足条件时返回该列表
    return  L

#定义列表
def sort_list(L):
    #调用递归函数quick_sort,传入left值和right值
    return  quick_sort(L,0,len(L)-1)

L = [5, 2, 5, 9, 1, 27, 8, 11, 6, 7, 2, 4]

print(sort_list(L))


