


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot=array[0]
        less_or_equal_than_pivot = [x for x in array[1:] if x <= pivot]
        large_than_pivot = [x for x in array[1:] if x > pivot]
        return quick_sort(less_or_equal_than_pivot) + [pivot]+ quick_sort(large_than_pivot)




if __name__ == '__main__':
    arr = [4,7,2,5,3,4,10,8,6,4]
    arr2 = quick_sort(arr)
    print(arr2)