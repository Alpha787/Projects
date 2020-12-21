import array as arr
mas = [2, 3, 2, 5, 4, 9, 8, 7, 5]
def len_mas(arr):
    array = []
    for i in range(1,len(arr)-1):
        if (arr[i] > arr[i+1]):
            array.append(arr[i])
    print(len(array))
len_mas(mas)
          











