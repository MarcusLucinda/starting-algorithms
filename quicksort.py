from random import randrange

def quicksort_worst(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_worst(less) + [pivot] + quicksort_worst(greater)

print(quicksort_worst([10, 12 , 11, 9, 13, 8, 12]))


def quicksort_best(array):
    if len(array) < 2:
        return array
    else:
        n = randrange(len(array))
        pivot = array.pop(n)
        less = [i for i in array if i <= pivot]
        greater = [i for i in array if i > pivot]
        return quicksort_best(less) + [pivot] + quicksort_best(greater)

print(quicksort_best([10, 12, 11, 9, 13, 8, 9, 2, 1, 4, 12]))