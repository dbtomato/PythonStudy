


def quick_sort(L):
    return q_sort(L,0,len(L) - 1)

def q_sort(L, left ,right):
    if left < right:
        pivot = Partition(L,left,right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def Partition(L, left, right):
    pivotKey = L[left]

    while left < right:
        while left < right and L[right] >= pivotKey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotKey:
            left += 1
        L[right] = L[left]

    L[left] = pivotKey
    return left

L = [4,7,2,5,3,4,10,8,6,4]
#L = [5, 9, 1, 11, 6, 7, 2, 4]

print(quick_sort(L))
'''

'''


