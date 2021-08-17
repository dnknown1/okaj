def bubble_sort(a):
    n = len(a)
    for j in range(n):
        for i in range(n-1):
            if a[i] >= a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        print(a)
    return a


print(bubble_sort([5,4,3,2,1]))