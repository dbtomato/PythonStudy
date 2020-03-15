

def insertionSort(array):
    if (len(array) <= 1):
        return array

    for i in range(1,len(array)):
        temp = array[i]
        #range(start, stop[, step])
        #start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
        #stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
        #step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
        for j in range(i-1, -1, -1):
            if array[j] > temp:
                array[j+1] = array[j]
                array[j] = temp

    return array


array=[4,7,2,5,3,4,10,8,6,4]

print(insertionSort(array))