
def bubbleSort(array,n):
    if n <= 1 :
        return array

    #设置标识位，False代表未交换
    flag = False
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
                #当数据交换时，将flag值改为True
                flag = True
        #如果未发生交换，则代表数组已经是有序的了，直接返回数组
        if not flag:
            return array
    return array




array=[4,7,2,5,3,4,10,8,6,4]

print(bubbleSort(array,len(array)))

