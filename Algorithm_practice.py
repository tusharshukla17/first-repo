# Insertion Sort
def insertion_sort(lst):
    index_range = range(1, len(lst))
    for i in index_range:
        value_to_sort = lst[i]
        while lst[i-1] > value_to_sort and i > 0:
            lst[i-1], lst[i] = lst[i], lst[i-1]
            i -= 1
    return lst


lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
insertion_sort(lst)
print(lst)

# Selection Sort


def selection_sort(lst):
    for i in range(len(lst)):
        mini_index = i
        for j in range(i+1, len(lst)):
            if lst[mini_index] > lst[j]:
                mini_index = j
        lst[mini_index], lst[i] = lst[i], lst[mini_index]


lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
selection_sort(lst)
print(lst)

# linear Search


def linear_search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
           print(i)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linear_search(lst, 5)


print("Hello World")




