def merge(arr,l,m,r):
    #n1+n2为数组的长度
    n1=m-l+1
    n2=r-m

    #创建临时数组
    L=[0]*(n1)
    R=[0]*(n2)

    #拷贝数据到临时数组 arrays L[]和R[]
    for i in range(0,n1):
        L[i]=arr[l+i]

    for j in range(0,n2):
        R[j]=arr[m+1+j]

    #归并到临时数组arr[l..r]中
    i=0    #初始化第一个子数组的索引
    j=0    #初始化第二个子数组的索引
    k=l    #初始归并子数组的索引

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i += 1
        else:
            arr[k]=R[j]
            j +=1
        k += 1

    #拷贝L[]的保留元素,此时K的坐标是上个循环后最后一位
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    #拷贝R[]的保留元素
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr,l,r):
    #l为0，r为arr的长度
    if l < r:
        #m为区间中间值
        m=int((l+(r-1)/2))
        #递归调用
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        #将分开的区间进行合并
        merge(arr,l,m,r)
    return  arr
# def mergeSort(arr,l,r):
#     if l < r:
#         m = int((l+(r-1))/2)
#         mergeSort(arr,l,m)
#         mergeSort(arr,m+1,r)
#         merge(arr,l,m,r)
#
#     return  arr


arr = [12, 11, 13, 8, 23, 7]
n = len(arr)
print("给定的数组")
for i in range(n):
    print("%d" % arr[i]),

mergeSort(arr, 0, n - 1)
print("\n\n排序后的数组")
for i in range(n):
    print("%d" % arr[i]),
