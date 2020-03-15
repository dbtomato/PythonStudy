#需要传入数组和数组的长度
def insert_sort(L,n):
    #如果数组长度小于等于1，直接返回，无需排序
    if n<=1:
        return
    #循环对比
    i=1
    while i<n:
        value = L[i]
        j = i - 1
        i += 1
        while j>0:
            if L[j]>value:
                #当满足条件时，将L[j]的值放到value的位置，value=L(j+1）
                L[j+1]=L[j]
            else:
                break
            j=j-1
        #需要将value的值放回到L(j)的位置
        L[j+1]=value
    return L

L=[7,9,5,13,11,24,12,8,5,21]
A=insert_sort(L,len(L))
print(A)



 